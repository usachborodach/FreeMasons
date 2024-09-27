import subprocess, os, playsound, time, threading, datetime
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



DevMode = False
if DevMode == True:
    Target = "192.168.254.99"
    ControlPointNumber = 1
    CheckIntervalSec = 30
else:
    Target = input("Введите адрес eмоива. Пример: 172.30.20.99\n")
    ControlPointNumber = int(input("Введите номер контрольной точки\n"))
    CheckIntervalSec = int(input("Введите интервал проверок в секундах. 30 будт норм\n"))

while True:
    AllocId = GetAllocId()
    if GetLogTail().find("Wagon") > -1:
        Log("Cостав пошёл!")
        threading.Thread(target=StartWarningSound, args=()).start()
    else:
        Log("Состав не идёт")
    Log(f"Ждём {CheckIntervalSec} секунд")
    time.sleep(CheckIntervalSec)

#вернуть фунцию - последний состав шёл тогда - то
#всплывающее окно
#Логирование
#Динамическое отображение таймаута