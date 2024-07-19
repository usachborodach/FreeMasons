import os
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)
Objects = {
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
Systems = {
    "Pto": ":80",
    "Nomad": ":4646",
    "Consul": ":8500",
    "RabbitMq": ":15672",
    "InfoProviderSwagger": ":50293/swagger",
    "DocumentServiceSwagger": ":7009/swagger"}
Header = ["Object"]
for System in Systems.keys():
    Header.append(System)
Table = list()
for Object, Address in Objects.items():
    Line = list()
    Line.append(Object)
    for System, Port in Systems.items():
        Line.append("http://"+Address+Port)
    Table.append(Line)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/", methods=["GET"])
def IndexPage():
    return render_template("index.html", Header=Header, Table=Table)
app.run(debug=True, host="10.11.1.32", port=5003)