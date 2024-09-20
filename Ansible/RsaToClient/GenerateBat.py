import json
ConciseDataPath = "c:\\FreeMasons\\TtmDb\\ConciseData.json"
ConciseData = json.loads(open(ConciseDataPath, encoding="utf-8").read())
BatFile = "cd C:\\FreeMasons\\Ansible\\RsaToClient\\NomadScripts\n"
for Item in ConciseData:
    Template = f"""nomad job run -detach -address=http://{Item["EmoivAddress"]}:4646 {Item["ObjectName"]}.hcl
start http://{Item["EmoivAddress"]}:4646/ui/jobs/RsaToClient
"""
    BatFile += Template
NomadScript = open("RunNomadScripts.bat", "w", encoding="UTF-8")
NomadScript.write(BatFile)
NomadScript.close()
print("done")