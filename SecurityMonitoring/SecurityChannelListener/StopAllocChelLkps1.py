import nomad, time, json
RemoteNomad = nomad.Nomad(host='10.11.21.99')
AllAllocations = RemoteNomad.job.get_allocations("SecurityMonitoring")
ChosenAllocations = []
for Allocation in AllAllocations:
    if Allocation["NodeName"] == "lkps1" and Allocation["ClientStatus"] == "running":
        RemoteNomad.allocation.stop_allocation(Allocation["ID"])
print("chelyabinsk lkps1 alloc restarted")