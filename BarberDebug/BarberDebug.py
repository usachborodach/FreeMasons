DevMode = True
CheckIntervalSec = 60
NumberOfConciseReports = 20

import time, json, requests, datetime
if DevMode == True:
    Target = "172.30.35.1:50293"
    ControlPointNumber = 1
    CheckIntervalSec = 5
else:
    Target = input("Введите адрес инфопровайдера. Пример: 172.30.19.99:50293\n")
    ControlPointNumber = int(input("Введите номер контрольной точки\n"))
def GetLatestConciseReports():
    print("Получаем краткий отчёт")
    RequestUrl = f'http://{Target}/GetLatestConciseReports?token=ifihadaheart&skip=0&take={NumberOfConciseReports}&onlyTroubles=false'
    try:
        ConciseReports = json.loads(requests.get(RequestUrl).text)
    except Exception as ExceptionText:
        input(ExceptionText)
        exit()
    else:
        return(ConciseReports)

for Train in GetLatestConciseReports()["result"]:
    if Train["trainType"] == 1 and Train["direction"] == 1 and Train["controlPoint"]["controlPointNumber"] == ControlPointNumber:
        LastTrainTime = datetime.datetime.strptime(Train["startedTime"][:16], "%Y-%m-%dT%H:%M")
        LastTrainDelta = (datetime.datetime.now() - LastTrainTime)
        print(f"Последний состав по этой точке проходил {str(LastTrainDelta)[:7]} назад")
        break
while True:
    print(f"Ждём {CheckIntervalSec} секунд")
    time.sleep(CheckIntervalSec)
    WeGotNewTrain = False
    for Train in GetLatestConciseReports()["result"]:
        if Train["trainType"] == 1 and Train["direction"] == 1 and Train["controlPoint"]["controlPointNumber"] == ControlPointNumber:
            if datetime.datetime.strptime(Train["startedTime"][:16], "%Y-%m-%dT%H:%M"):
                WeGotNewTrain = True
                break
    if WeGotNewTrain == True:        
        print("По интересующей нас точке прошёл состав!")
    else:
        print("По интересующей нас точке состав ещё не прошёл")
