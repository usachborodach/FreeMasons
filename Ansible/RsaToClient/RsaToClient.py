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
Rsa = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAG8Ypsw25QmkkSaWy87Gu3eqbK9c3S6B62E9cIlFEvk"

import json, os, subprocess
BasePath = os.path.dirname(__file__)
InputPath = "c:\\FreeMasons\\TtmDb\\ManualCheckedNodesData"
for Object in Objects:
	print(Object+" is started")
	ResultString = Head.replace("__OBJECTNAME__", Object)
	InputFilePath = os.path.join(InputPath, Object+".json")
	InputData = json.loads(open(InputFilePath, encoding="utf-8").read())
	for Node in InputData:
		if Node["Os"] == "linux":
			ResultString += Body.replace("__NODENAME__", Node["Name"]).replace("__RSA__", Rsa)
	ResultString += "}"
	print(ResultString)
	ResultPath = os.path.join(BasePath, Object+".hcl")
	NomadScript = open(ResultPath, "w", encoding="UTF-8")
	NomadScript.write(ResultString)
	NomadScript.close()
	subprocess.check_output("nomad job run --address=http://"+ObjectData["EmoivAddress"]+":4646 "+Object+".hcl").decode("utf-8")
	print(Object+" done")