import json, subprocess
GlobalConfig = json.loads(open("GlobalConfig.json", encoding="utf-8").read())
Template = open("NomadScriptTemplate.hcl", encoding="utf-8").read()
for Item in GlobalConfig:
    file = open("nomadscripts\\"+Item["__DATACENTER__"]+".hcl", "w")
    Result = Template
    for Key, Value in Item.items():
       Result = Result.replace(Key, str(Value).replace("\'", "\""))
    file.write(Result)
    file.close()
    print(Item["__DATACENTER__"])
    #try:
    #    print(subprocess.run("nomad job stop --purge --address=http://"+Item["__EXTERNALEMOIVADDRESS__"]+":4646 ReportsMonitoring", timeout = 10))
    #    print(subprocess.run("nomad job run --detach --address=http://"+Item["__EXTERNALEMOIVADDRESS__"]+":4646 "+"nomadscripts\\"+Item["__DATACENTER__"]+".hcl", timeout = 10))
    #except Exception as ExceptionText:
    #    print(ExceptionText)
