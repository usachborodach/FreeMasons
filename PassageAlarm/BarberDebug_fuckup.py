import time, json, requests, datetime, pymongo, playsound, os

BasePath = os.path.dirname(__file__)
WarnPath = os.path.join(BasePath, "warn.mp3")
def StartWarningSound():
    while True:
        playsound.playsound(WarnPath)

def GetReport(Url):
    while True:
        try:
            
        except Exception as ExceptionText:
            print(ExceptionText)
            print("Следующая попытка через 10 секунд")
            time.sleep(10)
            continue
        else:
            return(Train)

def GetLastTrain(Skip):
    print("Получаем краткий отчёт по составу")
    
    
    
    
    return(GetReport(RequestUrl)[0])

Aknowledged = list()
def IsAknowledged(Train):
    if Train["id"] in Aknowledged:
        print(f'Состав {Train["id"]} уже проверяли')
        return True
    else:
        print(f'Состав {Train["id"]} ещё не проверяли')
        Aknowledged.append(Train["id"])
        return False

def IsSuitable(Train):
    if 
        print(f'Состав {Train["id"]} удовлетворяет условиям')
        return True
    else:
        print(f'Поезд {Train["id"]} не удовлетворяет условиям')
        return False

def GetBarberWagons(Train):
    print(f"Получаем отчёт АРНВ для состава {Train['id']}")
    RequestUrl = f'http://{Target}/GetRailOCRReport?token=ifihadaheart&trainId={Train["id"]}'
    RailOCRReport = GetReport(RequestUrl)
    for WagonIndex, ReportLine in enumerate(RailOCRReport["result"]["reportLines"]):
        SkuNumber = ReportLine["actualWagonSKUNumber"]
        if SkuNumber == "--------" or SkuNumber == None:
            continue
        IsBarber = False
        for Document2651 in Collection2651.find( { "SkuNumber": SkuNumber }, {'TruckModels'} ):
            BarberModels = ["18-9810", "18-7020", "18-9855", "18-6863", "18-9800", "18-9836", "18-9836", "18-9817", "18-4129", "18-9891", "18-9750", "18-9889", "18-7033", "18-9890", "18-9829"]
            for TruckModel in BarberModels:
                if TruckModel in Document2651["TruckModels"]:
                    Url = f'http://{Target.split(":")[0]}/Wagon/{Train["id"]}/{WagonIndex+1}/15/1/1/33'
                    print(f"Состав {Train['id']}, вагон {WagonIndex} - тележка барбер\n{Url}")
                    IsBarber = True
        if IsBarber == False:
            print(f"Состав {Train['id']}, вагон {WagonIndex} - не барбер")

DevMode = True
if DevMode == True:
    Target = "172.30.20.99"
    ControlPointNumber = 2
    CheckIntervalSec = 30
else:
    Target = input("Введите адрес eмоива. Пример: 172.30.20.99\n")
    ControlPointNumber = int(input("Введите номер контрольной точки\n"))
    CheckIntervalSec = 60

MongoClient = pymongo.MongoClient(f"mongodb://{Target.split(':')[0]}:4000/")
PpssDb = MongoClient["PPSS-DB"]
Collection2651 = PpssDb["Document2651"]
Skip = 0
IsLastTrainTimeDefined = False




Skip = 0
while True:
    Train = json.loads(requests.get(RequestUrl = f'http://{Target}:50293/GetLatestConciseReports?token=ifihadaheart&skip={Skip}&take=1&onlyTroubles=false').text)["result"]
    if Train["trainType"] == 1 and Train["direction"] == 1 and Train["controlPoint"]["controlPointNumber"] == ControlPointNumber:
        print(f'Последний состав по этой точке проходил {str(datetime.datetime.now() - datetime.datetime.strptime(Train["startedTime"][:16], "%Y-%m-%dT%H:%M"))[:7]} назад')
        break
    else:
        Skip += 1
        continue



#всплывающее окно
#Логирование
#Динамическое отображение таймаута