import json, random
Data = json.loads(open("Result.json", encoding="utf-8").read())

while True:
    Entry = random.choice(Data)
    if Entry["category"] == "СЕМЬЯ":
        answer = input(Entry["hieroglyph"]+"\n")
        rightAnswer = Entry["translation"]
        if answer == rightAnswer:
            print("Молодец!")
        else:
            print("Неправильно!")
