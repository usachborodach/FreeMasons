import json, os
BasePath = os.path.dirname(__file__)
InputPath = os.path.join(BasePath, "..", "TtmDb", "ManualCheckedNodesData")


WinAppend = " ansible_user= ansible ansible_password=1234567Qw ansible_connection=winrm ansible_winrm_server_cert_validation=ignore"
for FileName in os.listdir(InputPath):
    
    if FileName != "chelyabinsk.json": # ВРЕМЯНКА!
        continue

    ObjectName = FileName.split(".")[0]
    LinuxGroup = f"""[linux:vars]
    ansible_user=root
    ansible_ssh_private_key_file=/home/gitlab-runner/.ssh/{ObjectName}_rsa
    ansible_become=yes
    ansible_become_method=enable
[linux]\n"""
    WindowsGroup = """[windows:vars]
    ansible_user= ansible
    ansible_password= 1234567Qw
    ansible_connection= winrm
    ansible_winrm_server_cert_validation= ignore
[windows]\n"""
    InputFilePath = os.path.join(InputPath, FileName)
    InputData = json.loads(open(InputFilePath, encoding="utf-8").read())
    for Node in InputData:
        if Node["Os"] == "linux":
            LinuxGroup += "    "+ObjectName+"_"+Node["Name"]+" ansible_host="+Node["Address"]+"\n"
        if Node["Os"] == "windows":
            WindowsGroup += "    "+ObjectName+"_"+Node["Name"]+" ansible_host="+Node["Address"]+"\n"
    ResultString = LinuxGroup + WindowsGroup
    Test = open("test.ini", "w", encoding="UTF-8")
    Test.write(ResultString)
    Test.close()
    print("done")
    exit()