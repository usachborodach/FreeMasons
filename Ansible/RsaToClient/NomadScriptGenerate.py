Head = """job "RsaToClient" {
	region = "global"
	datacenters = ["__OBJECTNAME__"]
	type = "batch"
"""		
Body = """	group "__NODENAME__" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "__NODENAME__"
        }
        task "task" {
			driver = "raw_exec"
			config {
				command = "/bin/bash"
				args = ["-c",
					<<SCRIPT
						FILE="/root/.ssh/authorized_keys"
						FOLDER="/root/.ssh"
						ssh_key="__RSA__"
						#Проверяем существует ли файл
						if [[ -f "$FILE" ]]
						then
						echo "$ssh_key" | tee -a /root/.ssh/authorized_keys > /dev/null 2>&1
						#Проверяем существует ли папка
						elif [[ -d "$FOLDER" ]]
						then
						echo > /root/.ssh/authorized_keys
						echo "$ssh_key" | tee -a /root/.ssh/authorized_keys > /dev/null 2>&1
						else
						mkdir /root/.ssh
						echo > /root/.ssh/authorized_keys
						echo "$ssh_key" | tee -a /root/.ssh/authorized_keys > /dev/null 2>&1
						fi
						#Вход под root по ssh разрешен только по ssh ключам и убрать вывод на экран
						echo 'PermitRootLogin without-password' | tee -a /etc/ssh/sshd_config > /dev/null 2>&1
						#Перезагрузка сервиса
						systemctl restart sshd
					SCRIPT
				]
			}
		}
	}
"""

Objects =["krasnoyarsk", "taman", "bataysk", "spb", "vhodnaya", "chelyabinsk", "oreh", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk", "ekaterinburg", "inskaya", "kinel", "losta"]
Objects =["habr"]
Rsa = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAG8Ypsw25QmkkSaWy87Gu3eqbK9c3S6B62E9cIlFEvk"

import json, os, subprocess
BasePath = os.path.dirname(__file__)
NodesDataPath = "c:\\FreeMasons\\TtmDb\\ManualCheckedNodesData"
ConciseDataPath = "c:\\FreeMasons\\TtmDb\\ConciseData.json"
ConciseData = json.loads(open(ConciseDataPath, encoding="utf-8").read())
for Object in Objects:
	print(Object+" is started")
	for Item in ConciseData:
		if Item["ObjectName"] == Object:
			EmoivAddress = Item["EmoivAddress"]
			break
	ResultString = Head.replace("__OBJECTNAME__", Object)
	ObjectNodesDataPath = os.path.join(NodesDataPath, Object+".json")
	InputData = json.loads(open(ObjectNodesDataPath, encoding="utf-8").read())
	for Node in InputData:
		if Node["Os"] == "linux":
			ResultString += Body.replace("__NODENAME__", Node["Name"]).replace("__RSA__", Rsa)
	ResultString += "}"
	ResultPath = os.path.join(BasePath, "NomadScripts", f"{Object}.hcl")
	NomadScript = open(ResultPath, "w", encoding="UTF-8")
	NomadScript.write(ResultString)
	NomadScript.close()
	try:
		print(subprocess.check_output(f'nomad job run -detach -address=http://{EmoivAddress}:4646 {ResultPath}').decode("utf-8"))
	except Exception as ExceptionText:
		print(ExceptionText)
	else:
		os.system(f"start http://{EmoivAddress}:4646/ui/jobs/RsaToClient")
	print(Object+" done")