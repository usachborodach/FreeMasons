AllObjects = ["krasnoyarsk", "bataysk", "spb", "vhodnaya", "habr", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
ChosenObjectList = ["chelyabinsk"]
ChosenObjectMode = False

import json, os, subprocess, datetime
from threading import Thread
BaseDir = os.path.dirname(os.path.abspath(__file__))
CommonConfig = json.loads(open(os.path.join(BaseDir, "..", "..", "CommonConfig.json"), encoding="utf-8").read())
def MainFunction(ExternalEmoivAddress, Datacenter):
    print("starting " + Datacenter)
    StartTime = datetime.datetime.now()
    try:
        subprocess.run("curl -X POST \"http://"+ExternalEmoivAddress+":5657/upload/share\" -H \"accept: application/json\" -H \"Content-Type: multipart/form-data\" -F \"file=@"+(os.path.join(BaseDir, "reports_monitoring_container.tar.gz")), timeout = 360)
    except Exception as ExceptionText:
        print(Datacenter + str(ExceptionText) + ". Duration: "  + str(datetime.datetime.now()-StartTime))
    else:
        print(" " + Datacenter + " container uploaded successfully. Duration: " + str(datetime.datetime.now()-StartTime))

for Object in CommonConfig:
    if ChosenObjectMode == True:
        if Object["__DATACENTER__"] in ChosenObjectList:
            Thread(target=MainFunction, args=(Object["__EXTERNALEMOIVADDRESS__"],Object["__DATACENTER__"],)).start()
    else:
        Thread(target=MainFunction, args=(Object["__EXTERNALEMOIVADDRESS__"],Object["__DATACENTER__"],)).start()