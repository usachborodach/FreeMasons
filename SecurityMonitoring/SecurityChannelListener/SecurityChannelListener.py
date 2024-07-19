import subprocess, os, nomad, requests, json, time, telebot, httplib2, sys
from datetime import datetime
h = httplib2.Http(".cache")
bot = telebot.TeleBot("5641565819:AAFS-GmkHOHXeK12TClRCZB_Gh8ZKRHBRQs")
LocalNomad = nomad.Nomad(host='localhost')
Argument = sys.argv[1]
def GetConfiguration():
    Configuration = {}
    Configuration = subprocess.check_output("consul kv get " + Argument, shell=True)
    Configuration = Configuration.decode("utf-8")
    Configuration = json.loads(Configuration)
    return(Configuration)
def CheckConfiguration():
    ConfigurationIsOk = True
    DefaultConfiguration = {
        "Datacenter": "chelyabinsk",
        "NodeName": "lkps1",
        "ChatId": -982279899,
        "ControlPoint": "1",
        "SendStartText": True,
        "SendStartPhoto": False,
        "SecurityChannel": "s1c6",
        "CheckIntervalSeconds": 15,
        "ContactBounceCheckIntervalSeconds": 3,
        "LogFilePath": "/mnt/Disk_1/CvLab/Common/Log/SecurityChannelListener.chelyabinsk_lkps1.log",
        "AlertingEnabled": True}
    for Key, Value in DefaultConfiguration.items():
        if Key not in Configuration.keys():
            Configuration[Key] = Value
            ConfigurationIsOk = False
    if ConfigurationIsOk == False:
        Log("Configuration was not ok. Try to put default keyvalues")
        ConfigurationStr = json.dumps(Configuration, indent=2)
        try:
            Result = subprocess.check_output("consul kv put " + Argument + " - <<EOF\n" + ConfigurationStr + "\nEOF", shell=True)
            Result = Result.decode("utf-8")
            Log(Result)
        except Exception as ExceptionText:
            Log(str(ExceptionText))
    else:
        Log("Configuration is ok")
def CheckLogFileExist():
    if os.path.isfile(LogFilePath) is False:
        f = open(Configuration["LogFilePath"], "x")
        f.close
def Log(Text):
    NewLine = str(datetime.now().strftime("%Y.%m.%d %H:%M:%S" )) + " " + Text
    print(NewLine)
    File = open(Configuration["LogFilePath"], "a")
    File.write(NewLine + "\n")
    File.close()
def SendStartMessage():
    if Configuration["SendStartText"] == True:
        SendText("SecurityChannelListener is started!\nConfiguration: " + str(Configuration))
    else:
        Log("SendStartText is false. Ignoring.")
    if Configuration["SendStartPhoto"] == True:
        ImageUrls = GetImageUrls()
        SendImages(ImageUrls)
    else:
        Log("SendStartPhoto is false. Ignoring.")
def GetMetricsUrl():
    AllocId = GetAllocId("RailOCR" + Configuration["ControlPoint"], "SensorProcessing")
    MetricsPort = GetDynamicPorts(AllocId, "PrometheusPort")
    MetricsPort = MetricsPort[0]
    MetricsUrl = "http://localhost:" + MetricsPort + "/metrics"
    return(MetricsUrl)
def GetSecurityChannelState(Metrics):
    Metrics = (Metrics.text)
    Metrics = Metrics.split("\n")
    for Line in Metrics:
        if Line.find("sensorprocessing_channel_current_states{flair=\"DI\",slot_and_channel=\"" + Configuration["SecurityChannel"] + "\"}") > -1:
            SecurityChannelState = Line[-1:]    
            return(SecurityChannelState)
def GetAllocId(Job, TaskGroupName):
    Allocations = LocalNomad.job.get_allocations("RailOCR" + Configuration["ControlPoint"])
    for Allocation in Allocations:
        if Allocation["TaskGroup"] == TaskGroupName:
            AllocId = Allocation["ID"]
            return(AllocId)
def GetDynamicPorts(AllocId, Label):
    Allocation = LocalNomad.allocation.get_allocation(AllocId)
    DynamicPorts = Allocation['Resources']['Networks'][0]['DynamicPorts']
    Ports = []
    for item in DynamicPorts:
        if item["Label"] == Label:
            Port = item["Value"]
            Port = str(Port)
            Ports.append(Port)
    return(Ports)
def SendText(InputText):
    for i in range(0, 10):
        Log(str(i + 1) + " of 10 try to send text: " + InputText)
        try:
            bot.send_message(Configuration["ChatId"], InputText)
        except telebot.apihelper.ApiTelegramException as ExceptionText:
            Log("Text sending error: " + str(ExceptionText))
            TimeToSleep = str(ExceptionText).split("after ")[1]
            Log("Next try after " + TimeToSleep + " seconds")
            time.sleep(int(TimeToSleep))
            continue
        except Exception as ExceptionText:
            Log("Undefined text sending error: " + str(ExceptionText))
            Log("Next try after 40 seconds")
            time.sleep(40)
            continue
        else:
            Log("Text sended succesfully: " + InputText)
            break
def GetImageUrls():
    AllocId = GetAllocId("RailOCR" + Configuration["ControlPoint"], "Lumberjack")
    Ports = GetDynamicPorts(AllocId, "imageProviderPort")
    ImageUrls = []
    for Port in Ports:
        ImageUrl = "http://192.168.254.1" + Configuration["ControlPoint"] + ":" + Port + "/camera/frame"
        ImageUrls.append(ImageUrl)
    return(ImageUrls)
def SendImages(ImageUrls):
    for ImageUrl in ImageUrls:
        Log("Try to download " + ImageUrl)
        try:
            response, content = h.request(ImageUrl)
        except Exception as ExceptionText:
            Log("Download image error: " + str(ExceptionText))
            continue
        else:
            file = open("image.jpg", "wb")
            file.write(content)
            file.close()
            Log(ImageUrl + " downloaded succesfully")
            Log(ImageUrl + " try to send")
            for i in range(0, 10):
                Log(str(i + 1) + " of 10 try to send image")
                try:
                    file = open("image.jpg", 'rb')
                    bot.send_photo(Configuration["ChatId"], file)
                except telebot.apihelper.ApiTelegramException as ExceptionText:
                    Log("Sending image error: " + str(ExceptionText))
                    TimeToSleep = str(ExceptionText).split("after ")[1]
                    Log("Next try after " + TimeToSleep + " seconds")
                    time.sleep(int(TimeToSleep))
                    continue
                except Exception as ExceptionText:
                    Log("Undefined image sending error: " + str(ExceptionText))
                    Log("Next try after 40 seconds")
                    time.sleep(40)
                    continue
                else:
                    Log("Image sended succesfully")
                    break              
Configuration = GetConfiguration()
CheckConfiguration()
Log("SecurityChannelListener is started")
Log("Configuration: " + str(Configuration))
SendStartMessage()
Log("Try to get MetricsUrl")
MetricsUrl = GetMetricsUrl()
Log("succesfully get MetricsUrl: " + MetricsUrl)
while True:
    try:
        try:
            Metrics = requests.get(MetricsUrl)
        except requests.exceptions.ConnectionError:
            Log(MetricsUrl + " requests.exceptions.ConnectionError")
            Log("Try to get new MetricsUrl")
            MetricsUrl = GetMetricsUrl()
            Log("succesfully get MetricsUrl: " + MetricsUrl)
            continue
        else:
            SecurityChannelState = "none"
            SecurityChannelState = GetSecurityChannelState(Metrics)
            Log("SecurityChannelState: " + SecurityChannelState)
            if Configuration["AlertingEnabled"] == True:
                if SecurityChannelState == "0":
                    Log("add " + str(Configuration["ContactBounceCheckIntervalSeconds"]) + " sec timeout, then retry")
                    time.sleep(Configuration["ContactBounceCheckIntervalSeconds"])
                    Metrics = requests.get(MetricsUrl)
                    SecurityChannelState = GetSecurityChannelState(Metrics)
                    if SecurityChannelState == "0":
                        SendText("ALERT! " + Configuration["Datacenter"] + " " + Configuration["NodeName"] + " SecurityChannelState: 0")
                        ImageUrls = GetImageUrls()
                        SendImages(ImageUrls)
        finally:
            time.sleep(Configuration["CheckIntervalSeconds"])
    except Exception as ExceptionText:
        Log("Global error: " + str(ExceptionText))