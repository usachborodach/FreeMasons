HostAddresses = {"localhost": "127.0.0.1", "vpn": "10.11.1.32:5003"}
ChosenAddress = "vpn"
import os
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)
Addresses = {
    "krasnoyarsk": "10.11.14.99",
    "taman": "172.30.15.1",
    "novorossiysk": "172.30.16.1",
    "bataysk": "172.30.17.1",
    "spb": "172.30.18.99",
    "vhodnaya": "172.30.19.99",
    "habr": "172.30.20.99",
    "chelyabinsk": "10.11.21.99",
    "oreh": "172.30.22.99",
    "zelecino": "172.30.23.1",
    "komsomolsk": "172.30.24.99",
    "smolensk": "172.30.29.99",
    "kurbakinskaya": "172.30.30.99",
    "murmansk": "10.11.31.99",
    "ekaterinburg": "172.30.32.1",
    "inskaya": "172.30.33.1",
    "kinel": "172.30.34.1",
    "losta": "172.30.35.1"}
Monkeys = {
    "krasnoyarsk": "empty",
    "taman": "empty",
    "novorossiysk": "empty",
    "bataysk": "http://172.30.17.11:5001",
    "spb": "http://172.30.18.141:5001",
    "vhodnaya": "http://172.30.19.141:5001",
    "habr": "http://172.30.20.142:5001",
    "chelyabinsk": "http://10.11.21.141:5001",
    "oreh": "http://172.30.22.141:5001",
    "zelecino": "http://172.30.23.81:5001",
    "komsomolsk": "http://172.30.24.81:5001",
    "smolensk": "http://172.30.29.81:5001",
    "kurbakinskaya": "http://172.30.30.81:5001",
    "murmansk": "http://10.11.31.81:5001",
    "ekaterinburg": "http://172.30.32.72:5001",
    "inskaya": "http://172.30.33.40:5001",
    "kinel": "http://172.30.34.21:5001",
    "losta": "http://172.30.35.40:5001"}
Systems = {
    "🚂 PtoWeb": ":80",
    "🐫 Nomad": ":4646",
    "👔 Consul": ":8500",
    "🐰 RabbitMq": ":15672",
    "👨🏻‍💻 InfoProv": ":50293/swagger",
    "📝 DocServ": ":7009/swagger"}
Colors = ["#9c27b0", "#4caf50", "#8bc34a", "#ff9800", "#f44336", "#03a9f4", "#009688", "#673ab7", "#00bcd4", "#cddc39", "#ff5722", "#ffc107", "#3f51b5", "#ffeb3b", "#e81e63", "#2196f3", "#4caf50", "#8bc34a"]
Table = list()
for Object, Address in Addresses.items():
    Row = dict()
    Row["Object"] = Object
    Row ["🐵 Monkey"] = Monkeys[Object]
    for System, Port in Systems.items():
        Row[System] = "http://"+Address+Port
    Table.append(Row)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/", methods=["GET"])
def IndexPage():
    return render_template("index.html", Table=Table, Colors=Colors)
app.run(debug=True, host=HostAddresses[ChosenAddress], port=5003)