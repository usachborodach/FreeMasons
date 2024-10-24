from flask import Flask, render_template, send_from_directory
import os, requests, json
app = Flask(__name__)

config = {"ExternalEmoivAddress": "172.30.19.99", "Datacenter": "vhodnaya"}
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/", methods=["GET"])
def return_index_page():
    json_input = json.loads(requests.get("http://172.30.19.141:5001").text)
    return render_template("index.html", json_input=json_input, config=config)

app.run(debug=True, host="0.0.0.0", port=5010)