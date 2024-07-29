HostAddresses = {"localhost": "127.0.0.1", "vpn": "10.11.1.32"}
ChosenAddress = "vpn"
import os, json
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)
BasePath = os.path.dirname(__file__)
DataPath = os.path.abspath(os.path.join(BasePath, "..", "TtmDb", "TtmDb.json"))
Data = json.loads(open(DataPath, encoding="utf-8").read())
Systems = {
    "🚂 ArmPto": ":80",
    "🐫 Nomad": ":4646",
    "👔 Consul": ":8500",
    "🐰 RabbitMq": ":15672",
    "👨🏻‍💻 InfoProv": ":50293/swagger",
    "📝 DocServ": ":7009/swagger"}
Colors = ["#9c27b0", "#4caf50", "#8bc34a", "#ff9800", "#f44336", "#03a9f4", "#009688", "#673ab7", "#00bcd4", "#cddc39", "#ff5722", "#ffc107", "#3f51b5", "#ffeb3b", "#e81e63", "#2196f3", "#4caf50", "#8bc34a"]
Sheet = list()
for Object in Data:
    Row = dict()
    Row["ObjectNumber"] = Object["EmoivAddress"].split(".")[2]
    Row["ObjectName"] = Object["ObjectName"]
    Row ["🐵 Monkey"] = Object["MonkeyAddress"]
    for System, Port in Systems.items():
        Row[System] = "http://"+Object["EmoivAddress"]
    Sheet.append(Row)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/", methods=["GET"])
def IndexPage():
    return render_template("index.html", Sheet=Sheet, Colors=Colors)
app.run(debug=True, host=HostAddresses[ChosenAddress], port=5003)