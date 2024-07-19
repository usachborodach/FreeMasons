import json, os, requests, subprocess
GlobalConfig = json.loads(open("GlobalConfig.json", encoding="utf-8").read())
Template = open("ConfigTemplate.json", encoding="utf-8").read()
for Item in GlobalConfig:
    file = open("configs\\"+Item["__DATACENTER__"]+".json", "w", encoding="utf-8")
    Result = Template
    for Key, Value in Item.items():
       Result = Result.replace(Key, str(Value).replace("\'", "\""))
       if Item["__DATACENTER__"] == "bataysk":
           Result = Result.replace("50293", "50985")
    file.write(Result)
    file.close()
    ConfigText = open("configs\\"+Item["__DATACENTER__"]+".json", encoding="utf-8").read()
    print(Item["__DATACENTER__"])
    try:
        print(subprocess.check_output("consul kv put -http-addr=http://"+Item["__EXTERNALEMOIVADDRESS__"]+":8500 tools/ReportsMonitoring @configs\\"+Item["__DATACENTER__"]+".json", timeout = 10).decode("utf-8"))
    except Exception as ExceptionText:
        print(ExceptionText)
input("all is done")