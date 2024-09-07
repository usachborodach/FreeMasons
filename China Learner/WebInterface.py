#переименовать мп3
#связать транскрипцию и мп3
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
    Item, Buttons = VanyaFunction(Data)
    return render_template("index.html", Item=Item, Buttons=Buttons)



def VanyaFunction(Data):
    while True:
        RandomItem = random.choice(Data)
        if RandomItem["category"] == "СЕМЬЯ":
            Question = RandomItem  
            del Question["translation"]
            break
    Variations = list()
    for i in range(3):
        Variation = dict()
        Variation["translation"] = random.choice(Data)["translation"]
        Variations.append(Variation)
    return(Question, Variations)



app.run(debug=True, host="0.0.0.0", port=5007)
# app.run(debug=True, host="10.11.1.32", port=5007)


