Target = "172.30.17.1"

import subprocess, json, os
BasePath = os.path.dirname(__file__)
KeysList = subprocess.check_output("consul kv get --keys --http-addr=http://"+Target+":8500 TechnoVisor/CameraHandler/").decode("utf-8").split("\n")

def JsonDump(Data, Path):
    with open(Path, 'w', encoding="utf-8") as fp:
        json.dump(Data, fp, indent=2, ensure_ascii=False)

def GetKeys():
    for KeyPath in KeysList:
        Key = json.loads(subprocess.check_output("consul kv get --http-addr=http://"+Target+":8500 "+KeyPath))
        JsonPath = os.path.join(BasePath, KeyPath.split("/")[-1]+".json")
        JsonDump(Key, JsonPath)
#def PutKeys()

GetKeys()