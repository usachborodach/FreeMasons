ChosenObjectMode = False
AllObjects = ["krasnoyarsk", "bataysk", "spb", "vhodnaya", "habr", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
ChosenObjectList = ["spb", "vhodnaya", "zelecino", "komsomolsk", "smolensk", "murmansk", "inskaya"]
UploadArtifact = True
Artifacts = ["dataharvester", "rmwebui"]
ChosenArtifact = 1
UploadTimeout = 360

import subprocess, json, os, time
from threading import Thread
from datetime import datetime
GlobalConfig = json.loads(open("GlobalConfig.json", encoding="utf-8").read())
LogFileName = "DeployAll.log"
file = open(LogFileName, "w")
file.close()
os.system("start "+LogFileName)
StartTime = datetime.now()
def Log(Text):
    Text = str(datetime.now())+" "+Text
    print(Text)
    Text = Text+"\n"
    file = open(LogFileName, "a")
    file.write(Text)
    file.close()
def MainFunction(ExternalEmoivAddress, Datacenter):
    Log(Datacenter+" started")
    try:
        if UploadArtifact == True:
            subprocess.run("""curl -X POST "http://"""+ExternalEmoivAddress+""":5657/upload/share" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@"""+Artifacts[ChosenArtifact]+"\\"+Artifacts[ChosenArtifact]+".tar.gz", timeout = UploadTimeout)
        subprocess.run("nomad job stop --purge --address=http://"+ExternalEmoivAddress+":4646 ReportsMonitoring", timeout = 10)
        time.sleep(1)
        subprocess.run("nomad job run --detach --address=http://"+ExternalEmoivAddress+":4646 "+"nomadscripts\\"+Datacenter+".hcl", timeout = 10)
    except Exception as ExceptionText:
        Log(Datacenter+" not finished. Duration: "+str(datetime.now()-StartTime))
        #Log(Datacenter+" "+str(ExceptionText))
    else:
        Log(Datacenter+" finished successfully. Duration: "+str(datetime.now()-StartTime))
for Object in GlobalConfig:
    if ChosenObjectMode == True:
        if Object["__DATACENTER__"] in ChosenObjectList:
            Thread(target=MainFunction, args=(Object["__EXTERNALEMOIVADDRESS__"],Object["__DATACENTER__"],)).start()
    else:
        Thread(target=MainFunction, args=(Object["__EXTERNALEMOIVADDRESS__"],Object["__DATACENTER__"],)).start()