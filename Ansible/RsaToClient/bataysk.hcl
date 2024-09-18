job "RsaToClient" {
	region = "global"
	datacenters = ["bataysk"]
	type = "batch"
	group "arnv1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "arnv1"
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
	group "arnv2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "arnv2"
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
	group "arnv3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "arnv3"
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
	group "element1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "element1"
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
	group "element2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "element2"
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
	group "element3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "element3"
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
	group "lkps2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lkps2"
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
	group "ppss-laz-gpu-1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "ppss-laz-gpu-1"
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
	group "telezhka2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "telezhka2"
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
	group "tvf1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvf1"
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
	group "tvf2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvf2"
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
	group "tvk1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvk1"
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