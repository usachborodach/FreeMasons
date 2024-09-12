AllObjects = ["krasnoyarsk", "taman", "novorossiysk", "bataysk", "spb", "vhodnaya", "habr", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
ChosenObjects = ["komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
import json, os, subprocess
BasePath = os.path.dirname(__file__)
ConciseDataPath = os.path.join(BasePath, "ConciseData.json")
ConciseData = json.loads(open(ConciseDataPath, encoding="utf-8").read())
for Index, ObjectData in enumerate(ConciseData):
    if ObjectData["ObjectName"] not in ChosenObjects:
        continue
    print(ObjectData["ObjectName"] + " is started")
    NodesData = list()
    NodesIdsStr = subprocess.check_output("nomad node status --address=http://"+ObjectData["EmoivAddress"]+":4646").decode("utf-8").split("\n")
    del NodesIdsStr[0]
    for Line in NodesIdsStr:
        if len(Line) == 0:
            continue
        Line = Line.split()
        NodesIdsDict = dict()
        if Line[2].startswith("arm"):
            continue
        NodesIdsDict["Id"] = Line[0]
        NodesIdsDict["Name"] = Line[2]
        NodesData.append(NodesIdsDict)
    Result = dict()
    for NodeData in NodesData:
        print(NodeData["Name"])
        NodeStatus = subprocess.check_output("nomad node status --verbose --address=http://"+ObjectData["EmoivAddress"]+":4646 "+NodeData["Id"]).decode("utf-8").split("\n")
        for Line in NodeStatus:
            if Line.find("unique.network.ip-address") > -1:
                Result[NodeData["Name"]] = Line.split()[-1]
                del NodeData["Id"]
                break
    SortedResult = dict(sorted(Result.items()))
    ResultPath = os.path.join(BasePath, "NodesDataFromNomad", ObjectData["ObjectName"]+".json")
    with open(ResultPath, 'w', encoding="utf-8") as fp:
        json.dump(SortedResult, fp, indent=2, ensure_ascii=False)
    print(ObjectData["ObjectName"] + " is finished")