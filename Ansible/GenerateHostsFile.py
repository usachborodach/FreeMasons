import json, os
BasePath = os.path.dirname(__file__)
InputPath = "c:\\FreeMasons\\TtmDb\\ManualCheckedNodesData"
FilesList = os.listdir(InputPath)
ObjectList = list()
for FileName in FilesList:
    ObjectList.append(FileName.split(".")[0])
LinuxVars = """[linux:vars]
system=linux
ansible_user=root
ansible_become=yes
ansible_become_method=enable
ansible_ssh_private_key_file=/rsa/keytoobjects
"""
LinuxChildren = "[linux:children]\n"
for Object in ObjectList:
    LinuxChildren += Object+"_linux\n"
ResultString = LinuxVars + LinuxChildren    
for FileName in FilesList:
    ObjectName = FileName.split(".")[0]
    LinuxGroup = f"[{ObjectName}_linux]\n"
    WindowsGroup = f"""[{ObjectName}_windows:vars]
ansible_user=ansible
ansible_password=1234567Qw
ansible_connection=winrm
ansible_winrm_server_cert_validation=ignore
[{ObjectName}_windows]\n"""
    InputFilePath = os.path.join(InputPath, FileName)
    InputData = json.loads(open(InputFilePath, encoding="utf-8").read())
    for Node in InputData:
        if Node["Os"] == "linux":
            LinuxGroup += ObjectName+"_"+Node["Name"]+" ansible_host="+Node["Address"]+"\n"
        if Node["Os"] == "windows":
            #WindowsGroup += ObjectName+"_"+Node["Name"]+" ansible_host="+Node["Address"]+"\n"
            continue
    ResultString += LinuxGroup #+ WindowsGroup
ResultPath = os.path.join(BasePath, "etc", "hosts.ini")
HostFile = open(ResultPath, "w", encoding="UTF-8")
HostFile.write(ResultString)
HostFile.close()
print("done")