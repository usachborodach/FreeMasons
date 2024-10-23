import os, subprocess, json
base_dir = os.path.dirname(os.path.abspath(__file__))
configurations_path = os.path.join(base_dir, "configurations")
for filename in os.listdir(configurations_path):
    address = (filename[:-4])
    config = json.loads(subprocess.check_output(f"consul kv get --http-addr={address}:8500 tools/ReportsMonitoring").decode("utf-8"))
    config_path = os.path.join(configurations_path, f"{address}.json")
    with open(config_path, 'w', encoding="utf-8") as fp:
        json.dump(config, fp, indent=2, ensure_ascii=False)