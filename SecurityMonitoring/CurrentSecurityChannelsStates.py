open("CurrentSecurityChannelsStates.log", "w").close()#каждый раз затирать лог
import requests, nomad, sys
from datetime import datetime
sys.path.append("C:\\ShuraRepo\\Modules\\")

Objects = ["krasnoyarsk", "bataysk", "piter", "omsk", "habarovsk", "chelyabinsk", "orehovo", "zelecino", "komsomolsk", "smolensk", "kurbakinskaya", "murmansk"]
VpnNumber = {"krasnoyarsk": "14", "bataysk": "17", "piter": "18", "omsk": "19", "habarovsk": "20", "chelyabinsk": "21", "orehovo": "22", "zelecino": "23", "komsomolsk": "24", "smolensk": "29", "kurbakinskaya": "30", "murmansk": "31"}
NumberOfControlPoints = {"krasnoyarsk": 2, "bataysk": 3, "piter": 2, "omsk": 4, "habarovsk": 2, "chelyabinsk": 5, "orehovo": 4, "zelecino": 1, "komsomolsk": 1, "smolensk": 2, "kurbakinskaya": 1, "murmansk": 1}
ObjectType = {"krasnoyarsk": "ppss", "bataysk": "ppss", "piter": "ppsswithouttk", "omsk": "ppsswithouttk", "habarovsk": "ppsswithouttk", "chelyabinsk": "ppss", "orehovo": "ppss", "zelecino": "tv", "komsomolsk": "tv", "smolensk": "tv", "kurbakinskaya": "tv", "murmansk": "tv"}
EmoivAdress = {"krasnoyarsk": "99", "bataysk": "1", "piter": "99", "omsk": "99", "habarovsk": "99", "chelyabinsk": "99", "orehovo": "99", "zelecino": "1", "komsomolsk": "99", "smolensk": "99", "kurbakinskaya": "99", "murmansk": "99"}
InfoproviderPort = {"krasnoyarsk": "50293", "bataysk": "50985", "piter": "50293", "omsk": "50293", "habarovsk": "50293", "chelyabinsk": "50293", "orehovo": "50293", "zelecino": "50293", "komsomolsk": "50293", "smolensk": "50293", "kurbakinskaya": "50293", "murmansk": "50293"}

def GetSecurityChannelState(Object, ControlPoint):
    EmoivUrl = "10.11." + VpnNumber[Object] + "." + EmoivAdress[Object]
    LocalNomad = nomad.Nomad(host = EmoivUrl)
    try:
        Allocations = LocalNomad.job.get_allocations("RailOCR" + ControlPoint)
    except Exception as ExceptionText:
        return (str(ExceptionText))
    for Allocation in Allocations:
        if Allocation["TaskGroup"] == "SensorProcessing":
            AllocId = Allocation["ID"]
    try:
        Allocation = LocalNomad.allocation.get_allocation(AllocId)
    except Exception as ExceptionText:
        return (str(ExceptionText))
    DynamicPorts = Allocation['Resources']['Networks'][0]['DynamicPorts']
    for item in DynamicPorts:
        if item["Label"] == "PrometheusPort":
            Port = item["Value"]
            Port = str(Port)
    if ObjectType[Object] == "ppss" or ObjectType[Object] == "ppsswithouttk":
        SensorProcessingServer = "3"
        PlcSlot = "1"
    if ObjectType[Object] == "tv":
        SensorProcessingServer = "1"
        PlcSlot = "0"
    MetricsUrl = "http://10.11." + VpnNumber[Object] + "." + SensorProcessingServer + ControlPoint + ":" + Port + "/metrics"
    try:
        Metrics = requests.get(MetricsUrl)
    except Exception as ExceptionText:
        return (str(ExceptionText))
    Metrics = (Metrics.text)
    Metrics = Metrics.split("\n")
    for Line in Metrics:
        if Line.find("sensorprocessing_channel_current_states{flair=\"DI\",slot_and_channel=\"s" + PlcSlot + "c6\"}") > -1:
            SecurityChannelState = Line[-1:]    
            return(SecurityChannelState)

def GetSecurityChannelStateBataysk(Object, ControlPoint):
    EmoivUrl = "10.11." + VpnNumber[Object] + "." + EmoivAdress[Object]
    LocalNomad = nomad.Nomad(host = EmoivUrl)
    try:
        Allocations = LocalNomad.job.get_allocations("RailOCR")
    except Exception as ExceptionText:
        return (str(ExceptionText))
    for Allocation in Allocations:
        if Allocation["TaskGroup"] == "CP" + ControlPoint + "-SensorProcessing":
            ID = Allocation["ID"]
    try:
        Allocation = LocalNomad.allocation.get_allocation(ID)
    except Exception as ExceptionText:
        return (str(ExceptionText))
    DynamicPorts = Allocation['Resources']['Networks'][0]['DynamicPorts']
    for item in DynamicPorts:
        if item["Label"] == "PrometheusPort":
            Port = item["Value"]
            Port = str(Port)
    if ObjectType[Object] == "ppss" or ObjectType[Object] == "ppsswithouttk":
        SensorProcessingServer = "3"
        PlcSlot = "1"
    if ObjectType[Object] == "tv":
        SensorProcessingServer = "1"
        PlcSlot = "0"
    SensorProcessingServers = {"1": "11", "2": "14", "3": "15"}
    MetricsUrl = "http://10.11." + VpnNumber[Object] + "." + SensorProcessingServers[ControlPoint] + ":" + Port + "/metrics"
    try:
        Metrics = requests.get(MetricsUrl)
    except Exception as ExceptionText:
        return (str(ExceptionText))
    Metrics = (Metrics.text)
    Metrics = Metrics.split("\n")
    for Line in Metrics:
        if Line.find("sensorprocessing_channel_current_states{flair=\"DI\",slot_and_channel=\"s" + PlcSlot + "c6\"}") > -1:
            SecurityChannelState = Line[-1:]    
            return(SecurityChannelState)

Choice = input("Введите интересующую КТ в формате \"chelyabinsk2\" или \"all\" для всех объектов:\n")

while True:
    if Choice == "all":
        for Object in Objects:
            print(Object)#
            CurrentNumberOfControlPoints = NumberOfControlPoints[Object]
            ControlPoints = [str(i) for i in range(1, CurrentNumberOfControlPoints + 1)]
            for ControlPoint in ControlPoints:
                if Object == "bataysk":
                    SecurityChannelState = GetSecurityChannelStateBataysk(Object, ControlPoint)
                else:    
                    SecurityChannelState = GetSecurityChannelState(Object, ControlPoint)
                print(str(datetime.now()) + " " + Object + ControlPoint + " SecurityChannelState: " + str(SecurityChannelState))
    else:
        Object = Choice[:-1]
        ControlPoint = Choice[-1:]
        SecurityChannelState = GetSecurityChannelState(Object, ControlPoint)
        print(str(datetime.now()) + " " + Object + ControlPoint + " SecurityChannelState: " + str(SecurityChannelState))
        input("Нажмите любую кнопку, чтобы повторить запрос...")