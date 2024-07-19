from flask import Flask, render_template, request
import json, os
app = Flask(__name__)

@app.route("/", methods=["GET"])
def IndexPage():
    Data = json.loads(open("Data.json", encoding="utf-8").read())
    return render_template("index.html", Data = Data)

@app.route("/ipmi/<address>", methods=["POST"])
def RunIpmiPage(address):
    os.system("start http://"+address.replace("172.30.", "172.31."))
    return IndexPage()

@app.route("/ping/<address>", methods=["POST"])
def RunPing(address):
    os.system("start cmd /k ping -t "+address)
    return IndexPage()

@app.route("/ssh/<address>", methods=["POST"])
def RunSsh(address):
    os.system("start cmd /k ssh user@"+address)
    return IndexPage()

@app.route("/rdp/<address>", methods=["POST"])
def RunRdp(address):
    os.system("cmdkey /generic:\""+address+"\" /user:\"user\" /pass: \"1234567Qw\"")
    os.system("mstsc /v:"+address)
    os.system("cmdkey /delete:"+address)
    #os.system("""for /F "tokens=1,2 delims= " %G in ('cmdkey /list ^| findstr Target') do cmdkey /delete %H""")
    return IndexPage()

@app.route("/nomad/<address>", methods=["POST"])
def RunNomadPage(address):
    os.system("start http://"+address+":4646")
    return IndexPage()

@app.route("/consul/<address>", methods=["POST"])
def RunConsulPage(address):
    os.system("start http://"+address+":8500")
    return IndexPage()

@app.route("/logviewer/<address>", methods=["POST"])
def RunLogviewerPage(address):
    os.system("start http://"+address+":11000")
    return IndexPage()

@app.route("/filebrowser/<address>", methods=["POST"])
def RunFilebrowserPage(address):
    os.system("start http://"+address+":11001")
    return IndexPage()

app.run(debug=True, host="localhost", port=5002)