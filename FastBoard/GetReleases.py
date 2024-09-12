import json, subprocess, os
BasePath = os.path.dirname(__file__)
DataPath = os.path.abspath(os.path.join(BasePath, "..", "TtmDb", "ConciseData.json"))
Data = json.loads(open(DataPath, encoding="utf-8").read())
for Item in Data:
    if Item["ObjectName"] in ["inskaya", "losta"]:
        JobName = "PPSS"
    else:
        JobName = "Ppss"    
    try:
        Definition = json.loads(subprocess.check_output("nomad job inspect --json --address=http://"+Item["EmoivAddress"]+":4646 "+JobName).decode("utf-8"))
    except Exception as ExceptionText:
        pass
    else:
        Release = Definition["TaskGroups"][0]["Tasks"][0]["Artifacts"][0]["GetterSource"].split("/d/")[1].split("/")[0]
        print(Item["EmoivAddress"] + "|" + Item["ObjectName"] + "|" + Release)
        Item["Release"] = Release
with open(DataPath, 'w', encoding="utf-8") as fp:
    json.dump(Data, fp, indent=2, ensure_ascii=False)
print("success")