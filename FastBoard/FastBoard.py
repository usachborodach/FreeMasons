import os, json
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)
BasePath = os.path.dirname(__file__)
Systems = {
    "🚂 ArmPto": ":80",
    "🐫 Nomad": ":4646",
    "👔 Consul": ":8500",
    "🐰 RabbitMq": ":15672",
    "👨🏻‍💻 InfoProv": ":50293/swagger",
    "📝 DocServ": ":7009/swagger"}
KirillColors = ["#CD5C5C", "#40E0D0", "#32CD32", "#C0C0C0", "#FFDAB9", "#8FBC8F", "#E9967A", "#7B68EE", "#9400D3", "#4682B4", "#228B22", "#FFFFE0", "#808000", "#DB7093", "#87CEEB", "#B22222", "#8A2BE2", "#1E90FF", "#40E0D0"]
BightColorsFromInternet = ["#9c27b0", "#4caf50", "#8bc34a", "#ff9800", "#f44336", "#03a9f4", "#009688", "#673ab7", "#00bcd4", "#cddc39", "#ff5722", "#ffc107", "#3f51b5", "#ffeb3b", "#e81e63", "#2196f3", "#4caf50", "#8bc34a"]
DarkColorsFromLibreCalc = ["#7b3d00", "#224b12", "#395511", "#8d281e", "#28471f", "#383d3c", "#4e102d", "#8d281e", "#706e0c", "#481d32", "#813709", "#784b04", "#481d32", "#4e102d", "#383d3c", "#224b12", "#28471f", "#395511"]

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/", methods=["GET"])
def IndexPage():
    DataPath = os.path.abspath(os.path.join(BasePath, "..", "TtmDb", "ConciseData.json"))
    Data = json.loads(open(DataPath, encoding="utf-8").read())
    Sheet = list()
    for Object in Data:
        Row = dict()
        Row["ObjectNumber"] = Object["EmoivAddress"].split(".")[2]
        Row["ObjectName"] = Object["ObjectName"]
        Row ["🐵 Monkey"] = Object["MonkeyAddress"]
        for System, Port in Systems.items():
            Row[System] = "http://"+Object["EmoivAddress"]+Port
        Row["Release"] = Object["Release"]
        Sheet.append(Row)
    return render_template("index.html", Sheet=Sheet, Colors=KirillColors)
app.run(debug=True, host="0.0.0.0", port=5003)
