job "RsaToClient" {
	region = "global"
	datacenters = ["ekaterinburg"]
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
	group "arnv4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "arnv4"
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
	group "arnv5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "arnv5"
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
	group "db1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "db1"
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
	group "db2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "db2"
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
	group "db3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "db3"
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
	group "db4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "db4"
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
	group "db5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "db5"
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
	group "emoiv" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "emoiv"
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
	group "fake1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "fake1"
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
	group "fake2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "fake2"
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
	group "fake3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "fake3"
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
	group "fake4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "fake4"
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
	group "fake5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "fake5"
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
	group "lkps1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lkps1"
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
	group "lkps3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lkps3"
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
	group "lkps4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lkps4"
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
	group "lkps5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lkps5"
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
	group "lpwan1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lpwan1"
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
	group "lpwan2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lpwan2"
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
	group "lpwan3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lpwan3"
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
	group "lpwan4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lpwan4"
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
	group "lpwan5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "lpwan5"
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
	group "rfid1" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "rfid1"
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
	group "rfid2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "rfid2"
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
	group "rfid3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "rfid3"
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
	group "rfid4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "rfid4"
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
	group "rfid5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "rfid5"
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
	group "tvf3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvf3"
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
	group "tvf4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvf4"
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
	group "tvf5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvf5"
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
	group "tvk2" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvk2"
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
	group "tvk3" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvk3"
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
	group "tvk4" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvk4"
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
	group "tvk5" {
        constraint {
            attribute = "${node.unique.name}"
            value     = "tvk5"
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