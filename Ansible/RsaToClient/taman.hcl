job "RsaToClient" {
	region = "global"
	datacenters = ["taman"]
	type = "batch"
	group "tv2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tv2"
        }
        task "task" {
			driver = "raw_exec"
			config {
				command = "/bin/bash"
				args = ["-c",
					<<SCRIPT
						FILE="/root/.ssh/authorized_keys"
						FOLDER="/root/.ssh"
						ssh_key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAG8Ypsw25QmkkSaWy87Gu3eqbK9c3S6B62E9cIlFEvk"
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
}