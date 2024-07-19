import nomad, time, json
NomadList = ["10.11.14.99", "10.11.18.99", "10.11.19.99", "10.11.20.99", "10.11.21.99", "10.11.22.99", "10.11.23.99", "10.11.24.99", "10.11.29.99", "10.11.30.99", "10.11.31.99"]
# NomadList = ["10.11.19.99"]
for RemoteNomadAddress in NomadList:
    RemoteNomad = nomad.Nomad(host=RemoteNomadAddress)
    try: 
        AllAllocations = RemoteNomad.job.get_allocations("SecurityMonitoring")
    except Exception as ExceptionText:
        print(RemoteNomadAddress + " Exception: " + str(ExceptionText))
        continue
    IdsToStop = []
    for Allocation in AllAllocations:
        if Allocation["ClientStatus"] == "running":
            IdsToStop.append(Allocation["ID"])
    for Id in IdsToStop:
        try: 
            RemoteNomad.allocation.stop_allocation(Id)
        except Exception as ExceptionText:
            print(RemoteNomadAddress + " " + Id + " Exception: " + str(ExceptionText))
        else:
            print(RemoteNomadAddress + " " + Id + " alloc restarted")
print("all avaible alloc restarted")