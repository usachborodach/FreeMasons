AllObjects = ["krasnoyarsk", "taman", "novorossiysk", "bataysk", "spb", "vhodnaya", "habr", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
ChosenObjects = ["komsomolsk"]
import json, os, subprocess
BasePath = os.path.dirname(__file__)
ConciseDataPath = os.path.join(BasePath, "ConciseData.json")
ConciseData = json.loads(open(ConciseDataPath, encoding="utf-8").read())
for Index, ObjectData in enumerate(ConciseData):
    if ObjectData["ObjectName"] not in ChosenObjects:
        continue
    print(ObjectData["ObjectName"] + " is started")
    NodesIdsStr = subprocess.check_output("nomad node status --address=http://"+ObjectData["EmoivAddress"]+":4646").decode("utf-8").split("\n")
    del NodesIdsStr[0]
    NodeNameIdDict = dict()
    for Line in NodesIdsStr:
        if len(Line) == 0:
            continue
        Line = Line.split()
        if Line[2].startswith("arm"):
            continue
        NodeNameIdDict[Line[2]] = Line[0]
    NodeNameIdDict = dict(sorted(NodeNameIdDict.items()))
    ResultData = list()
    for NodeName, Id in NodeNameIdDict.items():
        ResultNodeData = dict()
        ResultNodeData["Name"] = NodeName
        NodeStatus = subprocess.check_output("nomad node status --verbose --address=http://"+ObjectData["EmoivAddress"]+":4646 "+Id).decode("utf-8").split("\n")
        for Line in NodeStatus:
            if Line.find("unique.network.ip-address") > -1:
                ResultNodeData["Address"] = Line.split()[-1]
            if Line.find("kernel.name") > -1:
                ResultNodeData["Os"] = Line.split()[-1]
        ResultData.append(ResultNodeData)
        print(ObjectData["EmoivAddress"] + NodeName + " downloaded")
    ResultDataPath = os.path.join(BasePath, "NodesDataFromNomad", ObjectData["ObjectName"]+".json")
    with open(ResultDataPath, 'w', encoding="utf-8") as fp:
        json.dump(ResultData, fp, indent=2, ensure_ascii=False)
    print(ObjectData["ObjectName"] + " is finished")
print("All the script is finished")