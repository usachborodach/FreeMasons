import json
Data = json.loads(open("GlobalConfig.json", encoding="utf-8").read())

ProcessedData = list()
for Item in Data:
    Item["__EXTERNALEMOIVADDRESS__"] = "10.11.1x.99"
    ProcessedData.append(Item)

with open('GlobalConfigNew.json', 'w', encoding="utf-8") as fp:
    json.dump(ProcessedData, fp, indent=2, ensure_ascii=False)
