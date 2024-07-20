AllObjects = ["krasnoyarsk", "bataysk", "spb", "vhodnaya", "habr", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
ChosenObjectList = ["chelyabinsk"]
ChosenObjectMode = True

if ChosenObjectMode == True:
   ListToRestart = ChosenObjectList
else:
   ListToRestart = AllObjects
import json, subprocess, os, datetime, time
from threading import Thread
BaseDir = os.path.dirname(os.path.abspath(__file__))
GlobalConfig = json.loads(open(os.path.join(BaseDir, "..", "..", "CommonConfig.json"), encoding="utf-8").read())

def Log(Text):
    Text = str(datetime.datetime.now())+" "+Text
    print(Text)
    Text = Text+"\n"
    file = open(LogFilePath, "a")
    file.write(Text)
    file.close()

def GetExternalEmoivAddress(Object):
   for Item in GlobalConfig:
      if Item["__DATACENTER__"] == Object:
         return Item["__EXTERNALEMOIVADDRESS__"]

def MainFunction(Object):
   Log(Object + " is restarting")
   try:
      subprocess.run("nomad job stop --purge --address=http://"+GetExternalEmoivAddress(Object)+":4646 ReportsMonitoring", timeout = 60)
      subprocess.run("nomad job run --detach --address=http://"+GetExternalEmoivAddress(Object)+":4646 " + os.path.join(BaseDir, "GeneratedScripts", Object+".hcl"), timeout = 60)
   except Exception as ExceptionText:
      Log(Object + str(ExceptionText) + ". Duration: " + str(datetime.datetime.now()- StartTime))
   else:
      Log(Object + " is restarted successfully. Duration: " + str(datetime.datetime.now()- StartTime))

StartTime = datetime.datetime.now()
LogFilePath = os.path.join(BaseDir, "RestartJob.log")
file = open(LogFilePath, "w")
file.close()
os.system("start " + LogFilePath)
for Object in ListToRestart:
   Thread(target=MainFunction, args=(Object,)).start()
   if ChosenObjectMode == True:
      time.sleep(3)
      os.system("start http://"+GetExternalEmoivAddress(Object)+":4646/ui/jobs/ReportsMonitoring@default/ReportsMonitoring")