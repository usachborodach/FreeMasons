ObjectName = "ekaterinburg"
Address = "172.30.32.1"

import subprocess, json, os, base64
from pathlib import Path
BasePath = os.path.dirname(__file__)
def JsonDump(Data, Path):
    with open(Path, 'w', encoding="utf-8") as fp:
        json.dump(Data, fp, indent=2, ensure_ascii=False)
def CreateAndReturnPath(ConsulPath):
    PathToReturn = list()
    PathToReturn.append(BasePath)
    PathToReturn.append("data")
    PathToReturn.append("kv")
    PathToReturn.append(ObjectName)
    ShortConsulPath = ConsulPath.split("/")
    del ShortConsulPath[-1]
    PathToReturn += ShortConsulPath
    PathToReturn = '\\'.join(PathToReturn)
    PathToCreate = Path(PathToReturn)
    PathToCreate.mkdir(parents=True, exist_ok=True)
    if ConsulPath == ("monitoring/prometheus"):
        Extension = ".yml"
    elif ConsulPath.startswith("tools/LogViewer/"):
        Extension = ".txt"
    else:
        Extension = ".json"
    PathToReturn += "\\"+ConsulPath.split("/")[-1]+Extension
    return(PathToReturn)

KvExport = json.loads(subprocess.check_output("consul kv export --http-addr=http://"+Address+":8500").decode("utf-8"))
for Item in KvExport:
    if Item["value"] == "":
        continue
    if Item["key"].startswith("backups/"):
        continue
    PathToDump = CreateAndReturnPath(Item["key"])
    print(PathToDump)
    ConvertFrom64 = base64.b64decode(Item["value"]).decode("utf-8")
    if PathToDump.endswith(".yml") or PathToDump.endswith(".txt"):
        Result = open(PathToDump, "w", encoding="UTF-8")
        Result.write(ConvertFrom64)
        Result.close()
    else:
        JsonDump(json.loads(ConvertFrom64), PathToDump)
input("done")