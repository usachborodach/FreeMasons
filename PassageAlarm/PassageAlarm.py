import subprocess, os, playsound, time, threading, datetime, json, requests
BasePath = os.path.dirname(__file__)

def StartWarningSound():
    WarnPath = os.path.join(BasePath, "warn.mp3")
    while True:
        playsound.playsound(WarnPath)

def Log(Text):
    Text = f"{datetime.datetime.now()} {Text}"
    print(Text)
    if DevMode == True:
        Text += "\n"
        file = open("log.log", "a")
        file.write(Text)
        file.close()

def GetAllocId():
    JobStatus = subprocess.check_output(f"nomad job status --address=http://{Target}:4646 RailOCR{ControlPointNumber}", timeout = 10).decode("utf-8").split("\n")
    AllocationsIsReached = False
    for Line in JobStatus:
        if Line.find("Allocations") > -1:
            AllocationsIsReached = True
        if Line.find("SensorProcessing") > -1 and AllocationsIsReached == True:
            AllocId = Line.split()[0]
    return(AllocId)

def GetLogTail():
    LogTail = subprocess.check_output(f"nomad alloc logs --tail --address=http://{Target}:4646 {AllocId} SensorProcessing ", timeout = 10).decode("utf-8")
    Log(f"Хвост лога СП:\n{LogTail}")
    return(LogTail)

def CheckLastPassage():
    Skip = 0
    while True:
        Train = json.loads(requests.get(f'http://{Target}:50293/GetLatestConciseReports?token=ifihadaheart&skip={Skip}&take=1&onlyTroubles=false').text)["result"][0]
        if Train["trainType"] == 1 and Train["direction"] == 1 and Train["controlPoint"]["controlPointNumber"] == ControlPointNumber:
            print(f'Последний состав по этой точке проходил {str(datetime.datetime.now() - datetime.datetime.strptime(Train["startedTime"][:16], "%Y-%m-%dT%H:%M"))[:7]} назад')
            break
        else:
            Skip += 1
            continue

DevMode = True
if DevMode == True:
    Target = "172.30.19.99"
    ControlPointNumber = 1
    CheckIntervalSec = 30
else:
    Target = input("Введите адрес eмоива. Пример: 172.30.20.99\n")
    ControlPointNumber = int(input("Введите номер контрольной точки\n"))
    CheckIntervalSec = int(input("Введите интервал проверок в секундах. 30 будт норм\n"))

CheckLastPassage()
AllocId = GetAllocId()
while True:
    if GetLogTail().find("Wagon") > -1:
        Log("Cостав пошёл!")
        threading.Thread(target=StartWarningSound, args=()).start()
    else:
        Log(f"{Target} КТ: {ControlPointNumber} cостав не идёт")
    Log(f"Ждём {CheckIntervalSec} секунд")
    time.sleep(CheckIntervalSec)

#вывод эксепшена если что