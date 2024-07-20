import json, subprocess, os
BaseDir = os.path.dirname(os.path.abspath(__file__))
GlobalConfig = json.loads(open(os.path.join(BaseDir, "..", "..", "CommonConfig.json"), encoding="utf-8").read())
Template = open(os.path.join(BaseDir, "Template.hcl"), encoding="utf-8").read()
for Item in GlobalConfig:
    file = open(os.path.join(BaseDir, "GeneratedScripts", Item["__DATACENTER__"]+".hcl"), "w")
    Result = Template
    for Key, Value in Item.items():
       Result = Result.replace(Key, str(Value).replace("\'", "\""))
    file.write(Result)
    file.close()
    print(Item["__DATACENTER__"] + " generated sucessfully")