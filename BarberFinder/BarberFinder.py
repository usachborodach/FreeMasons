Target = input("Введите адрес инфопровайдера. Пример: 172.30.32.1:50293\n")
NumberOfTrainsForConciseReport = int(input("Введите количество составов для краткого отёта по составам. 100 будет норм.\n"))
TrainsToSkip = int(input("Введите количество составов, которые нужно пропустить. Нужно чтобы порыться в старых составах. Если нужны свежие - 0\n"))
ControlPointNumber = int(input("Введите номер контрольной точки\n"))
17
import requests, json, os, time
BasePath = os.path.dirname(__file__)

def JsonDump(Data, Path):
    with open(Path, 'w', encoding="utf-8") as fp:
        json.dump(Data, fp, indent=2, ensure_ascii=False)

def GetConciseReport():
    print("Получаем краткий отчёт")
    ReportUrl = "http://"+Target+"/GetLatestConciseReports?token=ifihadaheart&skip="+str(TrainsToSkip)+"&take="+str(NumberOfTrainsForConciseReport)+"&onlyTroubles=false"
    try:
        Data = json.loads(requests.get(ReportUrl).text)
    except Exception as ExceptionText:
        print(ExceptionText)
        input()
    return(Data)

def ProcessDataToRequest(ConciseReport):
    DataToTechnovisorReport = list()
    for Item in ConciseReport["result"]:
        if Item["trainType"] == 1 and Item["direction"] == 1 and Item["controlPoint"]["controlPointNumber"] == ControlPointNumber:
            Train = dict()
            Train["Id"] = Item["id"]
            Train["WagonsCount"] = Item["wagonsCount"]
            Train["LocomotivesCount"] = Item["locomotivesCount"]
            DataToTechnovisorReport.append(Train)
    return(DataToTechnovisorReport)

def GetTechnovisorReportsForOneTrain(Train):
    TechnovisorReportsForOneTrain = list()
    for WagonIndex in range(Train["LocomotivesCount"], Train["WagonsCount"]):
        TvfReportUrl = "http://"+Target+"/GetTechnovisorReport?token=ifihadaheart&trainId="+str(Train["Id"])+"&wagonIndex="+str(WagonIndex)
        print("Поезд: "+str(Train["Id"])+" Вагон: "+str(WagonIndex))
        TvfReport = json.loads(requests.get(TvfReportUrl).text)
        if TvfReport["errorCode"] == 1:
            print("Поезду не привязан отчёт техновизора. Пропускаем его.")
            return
        else:
            CheckForBarber(TvfReport, Train["Id"], WagonIndex)

def CheckForBarber(TvfReport, TrainId, WagonIndex):
    for Truck in TvfReport["result"]["trucks"]:
        for Block in Truck["blocks"]:
            if Block["sideC"]["isMultipartImage"] == True or Block["sideN"]["isMultipartImage"] == True:
                Url = "http://"+Target.split(":")[0]+"/Wagon/"+str(TrainId)+"/"+str(WagonIndex)+"/15/1/1/33"
                print("Мы нашли барбер! "+Url)
                time.sleep(1)
                os.system("start "+Url)
                input()
            else:
                print("Не барбер.")

ConciseReport = GetConciseReport()
DataToTechnovisorReport = ProcessDataToRequest(ConciseReport)
for Train in DataToTechnovisorReport:
    GetTechnovisorReportsForOneTrain(Train)
while(True):
    input("Мы достигли конца краткого отчета по составам. Перезапустите с другими параметрами, если не нашли барберов")