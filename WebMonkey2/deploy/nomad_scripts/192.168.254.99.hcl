job "ReportsMonitoring" {
	region = "global"
	datacenters = ["krasnoyarsk"]
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

		task "data_processing" {
			driver = "docker"
			artifact {
				source = "http://192.168.254.99:5657/share/reports_monitoring_container.tar.gz"
			}	
			artifact {
				source = "http://192.168.254.99:5657/share/reports_monitoring_artifacts.zip"
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
            	args = ["data_processing.py"]
				volumes = [
					"/etc/localtime:/etc/localtime",
					"/tmp/:/tmp/",
					"local/app:/app"]
			}
			resources {
				cpu = 100
				memory = 100
			}
		}

		task "json_output" {
			driver = "docker"
			artifact {
				source = "http://192.168.254.99:5657/share/reports_monitoring_container.tar.gz"
			}	
			artifact {
				source = "http://192.168.254.99:5657/share/reports_monitoring_artifacts.zip"
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
            	args = ["json_output.py"]
				volumes = [
					"/etc/localtime:/etc/localtime",
					"/var/log/:/var/log/",
					"/tmp/:/tmp/",
					"local/app:/app"]
			}
			resources {
				cpu = 100
				memory = 1000
			}
		}
	}
}