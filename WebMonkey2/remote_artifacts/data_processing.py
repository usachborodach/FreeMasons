import requests, json, base64, os, time
from datetime import datetime, timedelta
consul_response = (requests.get("http://localhost:8500/v1/kv/tools/ReportsMonitoring")).text
print(consul_response)
config = json.loads(base64.b64decode(json.loads(consul_response)[0]["Value"]).decode("utf-8"))

def get_latest_concise_reports():
    get_latest_concise_reports_url = f'http://{config["InfoProviderAddress"]}/GetLatestConciseReports?token=ifihadaheart&skip={config["GetLatestConciseReportsSkip"]}&take={config["GetLatestConciseReportsTake"]}&onlyTroubles=false'
    concise_report = json.loads(requests.get(get_latest_concise_reports_url).text)["result"]
    return(concise_report)

def direction_translate(direction):
    if direction == 1:
        return "➡️"
    if direction == 2:
        return "🔙"
        
def tgnl_check(concise_train_report):
    if concise_train_report["trainType"] != 1:
        return " "
    if concise_train_report["trainIndex"] == "∘∘∘∘ ∘∘∘ ∘∘∘∘":
        return "❌"
    if concise_train_report["trainIndex"] == None:
        return "❌"
    else:
        return "✔️"
        
def type_check(concise_train_report):
    if concise_train_report["trainTypeShortDesc"] == "-":
        return "❌"
    return concise_train_report["trainTypeShortDesc"]

def get_train_stats(concise_train_report):
    train_stats_url = f'http://{config["InfoProviderAddress"]}/diag/GetTrainStats?token=ifihadaheart&trainId={concise_train_report["id"]}'
    try:
        train_stats = json.loads(requests.get(train_stats_url).text)["result"]["subsystems"]
    except TypeError as exception_text:
        print(exception_text)
        return
    published_reports = list()
    timings = list()
    for published_report in train_stats:
        published_reports.append(published_report["issueName"])
        timings.append(round(published_report["processingTimeMaxMinutes"]))
    reports_status = dict()
    if concise_train_report["trainType"] != 1:
        for report_name in config["Reports"]:
            if report_name == "НВ":
                if report_name in published_reports:
                    reports_status["НВ"] = f'✔️ {timings[published_reports.index("НВ")]}'
                else:
                    reports_status["НВ"] = "❌"
            else:
                reports_status[report_name] = " "
    else:
        for report_name in config["Reports"]:
            if report_name in published_reports:
                reports_status[report_name] = f'✔️ {timings[published_reports.index(report_name)]}'
            else:
                reports_status[report_name] = "❌"
    return reports_status

def is_train_ready():
    if datetime.strptime(concise_train_report["startedTime"][:16], "%Y-%m-%dT%H:%M") > datetime.now() - timedelta(minutes = config["TimeoutReadyMinutes"]):
        return True
    else: False

print("DataHarvester is started")
while True:
    output = list()
    for concise_train_report in get_latest_concise_reports():
        processed_train_report = dict()
        processed_train_report["id"] = concise_train_report["id"]
        processed_train_report["КТ"] = concise_train_report["controlPoint"]["controlPointNumber"]
        processed_train_report["Наименование"] = concise_train_report["controlPoint"]["name"]
        if config["Datacenter"] == "bataysk":
            processed_train_report["Наименование"] = processed_train_report["Наименование"].split(">")[2].split("<")[0]
        processed_train_report["Дата"] = concise_train_report["startedTime"][5:10].replace("-", ".")
        processed_train_report["Время"] = concise_train_report["startedTime"][11:16]
        processed_train_report["Тип"] = type_check(concise_train_report) 
        processed_train_report["Лок"] = concise_train_report["locomotivesCount"]
        processed_train_report["Ваг"] = concise_train_report["wagonsCount"]
        processed_train_report["Напр."] = direction_translate(concise_train_report["direction"])
        processed_train_report["ТГНЛ"] = tgnl_check(concise_train_report)
        processed_train_report.update(get_train_stats(concise_train_report))
        if processed_train_report["ТГНЛ"] == "❌":
            for except_report in ["НГ", "ДКВ", "КМП", "ОД", "НП", "ЗО", "СГНС", "ОДВ"]:
                if except_report in processed_train_report.keys():
                    processed_train_report[except_report] = " "
        if processed_train_report["Напр."] == "🔙":
            processed_train_report["ФК"] = " "
            processed_train_report["ТК"] = " "
        output.append(processed_train_report)
    print(output)
    with open("/tmp/reports_monitoring.json", 'w', encoding="utf-8") as fp:
        json.dump(output, fp, indent=2, ensure_ascii=False)
    time.sleep(config["RefreshInterval"]*60)