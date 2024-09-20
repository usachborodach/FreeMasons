import pymongo, json, requests, time, os, datetime
from bson.json_util import dumps

Target = input("Введите адрес инфопровайдера. Пример: 172.30.19.99:50293\n")
NumberOfTrainsForConciseReport = int(input("Введите количество составов для краткого отёта по составам. 100 будет норм.\n"))
TrainsToSkip = int(input("Введите количество составов, которые нужно пропустить. Нужно чтобы порыться в старых составах. Если нужны свежие - 0\n"))
ControlPointNumber = int(input("Введите номер контрольной точки\n"))
TruckModels = [["18-9810", "18-7020", "18-9855", "18-6863", "18-9800", "18-9836", "18-9836", "18-9817", "18-4129", "18-9891", "18-9750", "18-9889", "18-7033", "18-9890", "18-9829"], ["18-194-1"]]
ChosenTruckModels = TruckModels[int(input("Выберите тип искомых тележек:\n0 - для барберов\n1 - для 18-194-1 (с юбкой)\n"))]

# Target = "172.30.35.1:50293"
# NumberOfTrainsForConciseReport = 100
# TrainsToSkip = 0
# ControlPointNumber = 417

MongoClient = pymongo.MongoClient(f"mongodb://{Target.split(':')[0]}:4000/")
PpssDb = MongoClient["PPSS-DB"]
Collection2651 = PpssDb["Document2651"]
print("Получаем краткий отчёт")
RequestUrl = f'http://{Target}/GetLatestConciseReports?token=ifihadaheart&skip={TrainsToSkip}&take={NumberOfTrainsForConciseReport}&onlyTroubles=false'
try:
    ConciseReport = json.loads(requests.get(RequestUrl).text)
except Exception as ExceptionText:
    input(ExceptionText)
    exit()
for Train in ConciseReport["result"]:
    TrainTime = datetime.datetime.strptime(Train["startedTime"][:16], "%Y-%m-%dT%H:%M")
    MatureTime = datetime.datetime.now() - datetime.timedelta(minutes=40)
    if TrainTime <  MatureTime and Train["trainType"] == 1 and Train["direction"] == 1 and Train["controlPoint"]["controlPointNumber"] == ControlPointNumber:
        print(f"Получаем отчёт АРНВ для состава {Train['id']}")
        RequestUrl = f'http://{Target}/GetRailOCRReport?token=ifihadaheart&trainId={Train["id"]}'
        try:
            RailOCRReport = json.loads(requests.get(RequestUrl).text)
        except Exception as ExceptionText:
            input(ExceptionText)
        for WagonIndex, ReportLine in enumerate(RailOCRReport["result"]["reportLines"]):
            SkuNumber = ReportLine["actualWagonSKUNumber"]
            if SkuNumber == "--------" or SkuNumber == None:
                continue
            IsBarber = False
            for Document2651 in Collection2651.find( { "SkuNumber": SkuNumber }, {'TruckModels'} ):
                for TruckModel in ChosenTruckModels:
                    if TruckModel in Document2651["TruckModels"]:
                        Url = f'http://{Target.split(":")[0]}/Wagon/{Train["id"]}/{WagonIndex+1}/15/1/1/33'
                        print(f"{SkuNumber} - оно!\n{Url}")
                        time.sleep(1)
                        os.system(f"start {Url}")
                        IsBarber = True
                        input()
            if IsBarber == False:
                print(f"{SkuNumber} - не то")



# with open('Document2651.json', 'w') as file:
#     file.write(dumps(Document2651))

# with open("RailOCRReport.json", 'w', encoding="utf-8") as fp:
#     json.dump(RailOCRReport, fp, indent=2, ensure_ascii=False)

# 91783373
# 18-9855