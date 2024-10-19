from flask import Flask, render_template, send_from_directory, request
from datetime import datetime, timedelta
import json, os, base64, requests
ConsulResponse = (requests.get("http://localhost:8500/v1/kv/tools/ReportsMonitoring")).text
print(ConsulResponse)
Config = json.loads(base64.b64decode(json.loads(ConsulResponse)[0]["Value"]).decode("utf-8"))
app = Flask(__name__)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/All", methods=["GET"])
def All():
    Data = list()
    FilesList = sorted(os.listdir(Config["DataPath"]))
    for FileName in reversed(FilesList):
        Data.append(json.loads(open(os.path.join(Config["DataPath"], FileName), encoding="utf-8").read()))
    return render_template("index.html", Data = Data, Config=Config)

@app.route("/OnlyTroublesCpSorted3h", methods=["GET"])
def OnlyTroublesCpSorted3h():
    Data = list()
    FilesList = sorted(os.listdir(Config["DataPath"]))
    for FileName in reversed(FilesList):
        TrainData = json.loads(open(os.path.join(Config["DataPath"], FileName), encoding="utf-8").read())
        if datetime.strptime("24"+TrainData["Дата"]+TrainData["Время"],"%y%m.%d%H:%M")<datetime.now()-timedelta(hours=3):
            continue
        if "❌" in TrainData.values():
            Data.append(TrainData)
    Data = sorted(Data, key=lambda TrainData: TrainData["КТ"])
    if len(Data) == 0:
        return render_template("index.html", Data=[{" ":"✔️ Всё ок", "  ": "Проблем нет", "-"*50: "-"*50}], Config=Config)
    return render_template("index.html", Data=Data, Config=Config)

@app.route("/", methods=["GET"])
def IndexPage():
    return OnlyTroublesCpSorted3h()
    
app.run(debug=True, host=Config["Host"], port=Config["Port"])