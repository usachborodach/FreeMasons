job "ReportsMonitoring" {
	region = "global"
	datacenters = ["komsomolsk"]
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
			value = "tvk1"
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
				source = "http://172.30.24.99:5657/share/reports_monitoring_container.tar.gz"
			}	
			artifact {
				source = "http://172.30.24.99:5657/share/reports_monitoring_artifacts.zip"
				destination = "local/app"
			}			
			kill_signal  = "SIGINT"
			kill_timeout = "1s"
			leader = false
			config {
				privileged = true
				force_pull = true
				network_mode = "host"
				image = "reports_monitoring_container"
				load = "reports_monitoring_container"
				command = "python"
            	args = ["dataharvester.py"]
				volumes = [
					"/etc/localtime:/etc/localtime",
					"/var/log/:/var/log/",
					"/data/ReportsMonitoring/:/data/ReportsMonitoring/",
					"local/app:/app"]
			}
			resources {
				cpu = 100
				memory = 100
			}
		}

		task "rmwebui" {
			driver = "docker"
			artifact {
				source = "http://172.30.24.99:5657/share/reports_monitoring_container.tar.gz"
			}	
			artifact {
				source = "http://172.30.24.99:5657/share/reports_monitoring_artifacts.zip"
				destination = "local/app"
			}			
			kill_signal  = "SIGINT"
			kill_timeout = "1s"
			leader = false
			config {
				privileged = true
				force_pull = true
				network_mode = "host"
				image = "reports_monitoring_container"
				load = "reports_monitoring_container"
				command = "python"
            	args = ["rmwebui.py"]
				volumes = [
					"/etc/localtime:/etc/localtime",
					"/var/log/:/var/log/",
					"/data/ReportsMonitoring/:/data/ReportsMonitoring/",
					"local/app:/app"]
			}
			resources {
				cpu = 100
				memory = 1000
			}
		}
	}
}