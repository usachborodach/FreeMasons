from flask import Flask, jsonify
import json, requests, base64, bson
consul_response = (requests.get("http://localhost:8500/v1/kv/tools/ReportsMonitoring")).text
print(consul_response)
config = json.loads(base64.b64decode(json.loads(consul_response)[0]["Value"]).decode("utf-8"))
app = Flask(__name__)
@app.route("/", methods=["GET"])
def index_page():
    data = json.loads(open("/tmp/reports_monitoring.json", encoding="utf-8").read())
    return jsonify(data)
app.run(debug=True, host=config["Host"], port=config["Port"])