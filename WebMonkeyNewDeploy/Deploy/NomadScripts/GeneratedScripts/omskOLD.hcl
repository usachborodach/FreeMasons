job "ReportsMonitoring" {
	region = "global"
	datacenters = ["vhodnaya"]
	type = "service"
	update {
		max_parallel = 1
		health_check = "checks"
		min_healthy_time = "1m"
		healthy_deadline = "5m"
		progress_deadline = "10m"
		auto_revert = false
		auto_promote = false
		canary = 0
		stagger = "5s"
	}


	group "ReportsMonitoring" {
		constraint {
			attribute = "${node.unique.name}"
			value = "fake1"
		}
		restart {
			interval = "30m"
			attempts = 3
			delay = "60s"
			mode = "delay"
		}


		task "dataharvester" {
			driver = "docker"
			artifact {
				source = "http://192.168.254.99:5657/share/dataharvester.tar.gz"
			}			
			kill_timeout = "50s"
			leader = false
			config {
				privileged = true
				force_pull = true
				network_mode = "host"
				image = "dataharvester"
				load = "dataharvester"
				args = [ "tools/ReportsMonitoring/DataHarvester"]
				volumes = [
					"/etc/localtime:/etc/localtime",
					"/var/log/:/var/log/",
					"/data/ReportsMonitoring/:/data/ReportsMonitoring/"]
			}
			resources {
				cpu = 100
				memory = 300
			}
		}


		task "rmwebui" {
			driver = "docker"
			artifact {
				source = "http://192.168.254.99:5657/share/rmwebui.tar.gz"
			}			
			kill_timeout = "50s"
			leader = false
			config {
				privileged = true
				force_pull = true
				network_mode = "host"
				image = "rmwebui"
				load = "rmwebui"
				args = [ "tools/ReportsMonitoring/WebUI"]
				volumes = ["/data/ReportsMonitoring/:/data/ReportsMonitoring/"]					
			}
			resources {
				cpu = 100
				memory = 300
				network {
					port "MainServicePort" {
						static = "5001"
						host_network = "default"
					}
				}
			}
		}
		
		
	}
}