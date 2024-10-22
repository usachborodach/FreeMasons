import requests, json, base64, os, time
from datetime import datetime, timedelta
StartTime = datetime.now()
ConsulResponse = (requests.get("http://localhost:8500/v1/kv/tools/ReportsMonitoring")).text
print(ConsulResponse)
Config = json.loads(base64.b64decode(json.loads(ConsulResponse)[0]["Value"]).decode("utf-8"))

if os.path.exists(Config["DataPath"]) == False:
    os.makedirs(Config["DataPath"])
if os.path.isfile(Config["LogPath"]) == False:
    file = open(Config["LogPath"], 'a')
    file.close()

def Log(Text):
    Text = str(datetime.now())+" "+Text
    print(Text)
    Text = Text+"\n"
    file = open(Config["LogPath"], "a")
    file.write(Text)
    file.close()

Log("ConsulResponse: " + ConsulResponse)

if Config["СlearLog"] == True:
    Log("СlearLog = True. Сlear log.")
    file = open(Config["LogPath"], 'w')
    file.close()
if Config["СlearData"] == True:
    Log("СlearData = True. Removing files.")
    for File in os.listdir(Config["DataPath"]):
        os.remove(Config["DataPath"]+File)

def JsonDump(Data, Filename):
    with open(f"{Filename}.json", 'w', encoding="utf-8") as fp:
        json.dump(Data, fp, indent=2, ensure_ascii=False)

def DumpIssuesToDatabase(Data):
    if "❌" in Data.values():
        Log(str(Data["id"])+" got issues")
        Issues = dict()
        Issues["Datacenter"] = Config["Datacenter"]
        Issues["ExternalEmoivAddress"] = Config["ExternalEmoivAddress"]
        Issues["TrainId"] = str(Data["id"])
        Issues["КТ"] = str(Data["КТ"])
        Issues["Наименование"] = Data["Наименование"]
        Issues["Дата"] = Data["Дата"]
        Issues["Время"] = Data["Время"]
        Issues["Тип"] = str(Data["Тип"])
        Issues["Лок"] = str(Data["Лок"])
        Issues["Ваг" ] = str(Data["Ваг"])
        Issues["Issues"] = list()
        for Key, Value in Data.items():
            if Value == "❌":
                Issues["Issues"].append(Key)
        try:
            Log(str(Data["id"])+" try to dump in remote database")
            # Collection.insert_one(Issues).inserted_id
        except Exception as ExceptionText:
            Log(str(ExceptionText))
        else:  
            Log(str(Data["id"])+" dumped to remote database successfully")
    else:
        Log(str(Data["id"])+" got no issues. Nothing to dump in remote database")
        
def GetLatestConciseReports():
    LatestConciseReportsUrl = "http://" + Config["InfoProviderAddress"] + "/GetLatestConciseReports?token=ifihadaheart&skip=0&take=" + str(Config["NumberOfTrainsForConciseReport"]) + "&onlyTroubles=false"
    Log("Try to get " + LatestConciseReportsUrl)
    ConciseReport = json.loads(requests.get(LatestConciseReportsUrl).text)["result"]
    Log("GetLatestConciseReports recieved successfully")
    return(ConciseReport)

def DirectionTranslator(Direction):
    if Direction == 1:
        return "➡️"
    if Direction == 2:
        return "🔙"
        
def TgnlCheck(ConciseTrainReport):
    if ConciseTrainReport["trainType"] != 1:
        return " "
    if ConciseTrainReport["trainIndex"] == "∘∘∘∘ ∘∘∘ ∘∘∘∘":
        return "❌"
    if ConciseTrainReport["trainIndex"] == None:
        return "❌"
    else:
        return "✔️"
        
def TypeCheck(ConciseTrainReport):
    if ConciseTrainReport["trainTypeShortDesc"] == "-":
        return "❌"
    return ConciseTrainReport["trainTypeShortDesc"]

def GetTrainStats(ConciseTrainReport):
    TrainStatsUrl = "http://" + Config["InfoProviderAddress"] + "/diag/GetTrainStats?token=ifihadaheart&trainId=" + str(ConciseTrainReport["id"])
    Log("try to get " + TrainStatsUrl)
    TrainStats = json.loads(requests.get(TrainStatsUrl).text)["result"]["subsystems"]
    PublishedReports = list()
    Timings = list()
    for PublishedReport in TrainStats:
        PublishedReports.append(PublishedReport["issueName"])
        Timings.append(round(PublishedReport["processingTimeMaxMinutes"]))
    ReportsStatus = dict()
    if ConciseTrainReport["trainType"] != 1:
        for ReportName in Config["Reports"]:
            if ReportName == "НВ":
                if ReportName in PublishedReports:
                    ReportsStatus["НВ"] = "✔️"+str(Timings[PublishedReports.index("НВ")])
                else:
                    ReportsStatus["НВ"] = "❌"
            else:
                ReportsStatus[ReportName] = " "
    else:
        for ReportName in Config["Reports"]:
            if ReportName in PublishedReports:
                ReportsStatus[ReportName] = "✔️"+str(Timings[PublishedReports.index(ReportName)])
            else:
                ReportsStatus[ReportName] = "❌"
    return ReportsStatus


    
Log("DataHarvester is started")
while True:
    ThereIsNoNewTrains = True
    FilesList = sorted(os.listdir(Config["DataPath"]))
    ProcessedTrains = list()
    for Filename in FilesList:
        ProcessedTrains.append(Filename[:-5])
    for ConciseTrainReport in GetLatestConciseReports():
        if str(ConciseTrainReport["id"]) in ProcessedTrains:
            Log("Train "+str(ConciseTrainReport["id"])+" already processed")
            continue
        else:
            Log("Train "+str(ConciseTrainReport["id"])+" is not processed")
        if datetime.strptime(ConciseTrainReport["startedTime"][:16], "%Y-%m-%dT%H:%M") > datetime.now() - timedelta(minutes = Config["TimeoutReadyMinutes"]):
            Log("Train "+str(ConciseTrainReport["id"])+" is not ready")
            continue
        else:
            ProcessedTrainReport = dict()
            ProcessedTrainReport["id"] = ConciseTrainReport["id"]
            ProcessedTrainReport["КТ"] = ConciseTrainReport["controlPoint"]["controlPointNumber"]
            ProcessedTrainReport["Наименование"] = ConciseTrainReport["controlPoint"]["name"]
            if Config["Datacenter"] == "bataysk":
                ProcessedTrainReport["Наименование"] = ProcessedTrainReport["Наименование"].split(">")[2].split("<")[0]
            ProcessedTrainReport["Дата"] = ConciseTrainReport["startedTime"][5:10].replace("-", ".")
            ProcessedTrainReport["Время"] = ConciseTrainReport["startedTime"][11:16]
            ProcessedTrainReport["Тип"] = TypeCheck(ConciseTrainReport) 
            ProcessedTrainReport["Лок"] = ConciseTrainReport["locomotivesCount"]
            ProcessedTrainReport["Ваг"] = ConciseTrainReport["wagonsCount"]
            ProcessedTrainReport["Напр."] = DirectionTranslator(ConciseTrainReport["direction"])
            ProcessedTrainReport["ТГНЛ"] = TgnlCheck(ConciseTrainReport)
            try:
                ProcessedTrainReport.update(GetTrainStats(ConciseTrainReport))
            except Exception as ExceptionText:
                Log(str(ExceptionText))
                continue
            if ProcessedTrainReport["ТГНЛ"] == "❌":
                for ExceptReport in ["НГ", "ДКВ", "КМП", "ОД", "НП", "ЗО", "СГНС", "ОДВ"]:
                    if ExceptReport in ProcessedTrainReport.keys():
                        ProcessedTrainReport[ExceptReport] = " "
            if ProcessedTrainReport["Напр."] == "🔙":
                ProcessedTrainReport["ФК"] = " "
                ProcessedTrainReport["ТК"] = " "
            JsonDump(ProcessedTrainReport, (os.path.join(Config["DataPath"], str(ConciseTrainReport["id"]))))
            Log(str(ConciseTrainReport["id"])+" dumped to file successfully")
            #DumpIssuesToDatabase(ProcessedTrainReport)
            ThereIsNoNewTrains = False
    Log("Main iteration successfully done. ThereIsNoNewTrains="+str(ThereIsNoNewTrains))
    if ThereIsNoNewTrains == True:
        Log("Wait for ConciseReportIntervalMinutes: "+str(Config["ConciseReportIntervalMinutes"]))
        time.sleep(Config["ConciseReportIntervalMinutes"]*60)