AllObjects = ["krasnoyarsk", "bataysk", "spb", "vhodnaya", "habr", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
ChosenObjectMode = False
ChosenObjectList = ["vhodnaya"]

if ChosenObjectMode == True:
   ListToUpload = ChosenObjectList
else:
   ListToUpload = AllObjects
import json, os, subprocess, datetime, shutil
from threading import Thread
BaseDir = os.path.dirname(os.path.abspath(__file__))
CommonConfig = json.loads(open(os.path.join(BaseDir, "..", "..", "CommonConfig.json"), encoding="utf-8").read())
def Log(Text):
    Text = str(datetime.datetime.now())+" "+Text
    print(Text)
    Text = Text+"\n"
    file = open(LogFilePath, "a")
    file.write(Text)
    file.close()
def GetExternalEmoivAddress(Object):
   for Item in CommonConfig:
      if Item["__DATACENTER__"] == Object:
         return Item["__EXTERNALEMOIVADDRESS__"]
def MainFunction(Object):
    print("starting " + Object)
    StartTime = datetime.datetime.now()
    try:
        Log(f"{Object} artifacts loading have been started")
        subprocess.run("curl -X POST \"http://"+GetExternalEmoivAddress(Object)+":5657/upload/share\" -H \"accept: application/json\" -H \"Content-Type: multipart/form-data\" -F \"file=@"+(os.path.join(BaseDir, "reports_monitoring_artifacts.zip")), timeout = 360)
    except Exception as ExceptionText:
        Log(Object + str(ExceptionText) + ". Duration: "  + str(datetime.datetime.now()-StartTime))
    else:
        Log(f"{Object} artifacts uploaded successfully. Duration: {str(datetime.datetime.now()-StartTime)}")

LogFilePath = os.path.join(BaseDir, "UploadArtifacts.log")
file = open(LogFilePath, "w")
file.close()
os.system("start " + LogFilePath)
shutil.make_archive(os.path.join(BaseDir, "reports_monitoring_artifacts"), 'zip', os.path.join(BaseDir, "..", "..", "Artifacts"))
Log("Zip archive was created succesfully")
for Object in ListToUpload:
    Thread(target=MainFunction, args=(Object,)).start()