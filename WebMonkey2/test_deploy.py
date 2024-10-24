address = "172.30.19.99"
import os, subprocess, shutil, time
BaseDir = os.path.dirname(os.path.abspath(__file__))
shutil.make_archive(os.path.join(BaseDir, "deploy", "zipped_artifacts", "reports_monitoring_artifacts"), 'zip', os.path.join(BaseDir, "remote_artifacts"))
subprocess.run(f"curl -X POST \"http://{address}:5657/upload/share\" -H \"accept: application/json\" -H \"Content-Type: multipart/form-data\" -F \"file=@"+(os.path.join(BaseDir, "deploy", "zipped_artifacts", "reports_monitoring_artifacts.zip")), timeout = 360)
print()
subprocess.run(f"consul kv put --http-addr={address}:8500 tools/ReportsMonitoring @{os.path.join(BaseDir, 'deploy', 'configurations', address+'.json')}", timeout = 60)
subprocess.run(f"nomad job stop --purge --address=http://{address}:4646 ReportsMonitoring", timeout = 60)
subprocess.run(f"nomad job run --detach --address=http://{address}:4646 {os.path.join(BaseDir, 'deploy', 'nomad_scripts', address)}.hcl", timeout = 60)
time.sleep(3)
os.system(f"start http://172.30.19.141:5001")
os.system(f"start http://{address}:4646/ui/jobs/ReportsMonitoring@default/ReportsMonitoring")