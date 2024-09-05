#добавить кнопки
#оформить это функцией, чтобы Ваня мог прописать логику

from flask import Flask, render_template, send_from_directory, send_file
import json, os, random
app = Flask(__name__)
Data = json.loads(open("data.json", encoding="utf-8").read())
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/", methods=["GET"])
def IndexPage():
    while True:
        RandomItem = random.choice(Data)
        if RandomItem["category"] == "СЕМЬЯ":
            break
    return render_template("index.html", Item=RandomItem, Buttons=["Кнопка раз", "Кнопка два", "Кнопка три"])


app.run(debug=True, host="0.0.0.0", port=5007)
# app.run(debug=True, host="10.11.1.32", port=5007)


