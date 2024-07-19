AllObjects = ["krasnoyarsk", "bataysk", "spb", "vhodnaya", "habr", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
ChosenObjectList = ["vhodnaya", "kurbakinskaya"]

import json, os, subprocess, datetime
BaseDir = os.path.dirname(os.path.abspath(__file__))
CommonConfig = json.loads(open(os.path.join(BaseDir, "..", "..", "CommonConfig.json"), encoding="utf-8").read())
for Object in CommonConfig:
    print("starting "+Object["__DATACENTER__"])
    StartTime = datetime.datetime.now()
    try:
        subprocess.run("curl -X POST \"http://"+Object["__EXTERNALEMOIVADDRESS__"]+":5657/upload/share\" -H \"accept: application/json\" -H \"Content-Type: multipart/form-data\" -F \"file=@"+(os.path.join(BaseDir, "reports_monitoring_container.tar.gz")), timeout = 360)
    except Exception as ExceptionText:
        print(ExceptionText)
    else:
        print(" "+Object["__DATACENTER__"]+" container uploaded successfully. Duration: "+str(datetime.datetime.now()-StartTime))