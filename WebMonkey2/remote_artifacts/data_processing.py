import requests, json, base64, time
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

def get_headers():
    default_headers = ["id", "КТ", "Наименование", "Дата", "Время", "Тип", "Лок", "Ваг", "Напр", "ТГНЛ"]
    result_headers = default_headers + config["Reports"]
    return result_headers

def data_dump(data):
    with open("/tmp/reports_monitoring.json", 'w', encoding="utf-8") as fp:
        json.dump(data, fp, indent=2, ensure_ascii=False)

def get_reports_stats(train_id):
    reports_stats = list()
    train_stats_url = f'http://{config["InfoProviderAddress"]}/diag/GetTrainStats?token=ifihadaheart&trainId={train_id}'
    try:
        train_stats = json.loads(requests.get(train_stats_url).text)["result"]["subsystems"]
    except TypeError as exception_text:
        print(exception_text)
        for train_report in config["Reports"]:
            reports_stats.append(str())
    else:
        for train_report in config["Reports"]:
            reports_stats.append("❌")
            for published_report in train_stats:
                if published_report["issueName"] == train_report:
                    reports_stats[-1] = (f'✔️ {round(published_report["processingTimeMaxMinutes"])}')
    return reports_stats

def remove_alarms_for_noncargo(row):
    if row[get_headers().index("Тип")] != "Г":
        for index, cell in enumerate(row):
            if type(cell) is str:
                row[index] = cell.replace("❌", str())
    return row

def remove_alarms_if_tgnl_absent(row):
    tgnl_addicted_reports = ["НГ", "ДКВ", "КМП", "ОД", "НП", "ЗО", "СГНС", "ОДВ"]
    if row[get_headers().index("ТГНЛ")] == "❌":
        for report in tgnl_addicted_reports:
            if row[get_headers().index(report)] == "❌":
                row[get_headers().index(report)] = str()
    return row

def remove_tv_alarms_for_reverse(row):
    if row[get_headers().index("Напр")] == "🔙":
        if "ФК" in config["Reports"]:
            row[get_headers().index("ФК")] = str()
        if "ТК" in config["Reports"]:
            row[get_headers().index("ТК")] = str()
    return row

def remove_alarms_for_raw_trains(row, concise_train_report):
    if datetime.strptime(concise_train_report["startedTime"][:16], "%Y-%m-%dT%H:%M") > datetime.now() - timedelta(minutes=config["TimeoutReadyMinutes"]):
        for index, cell in enumerate(row):
            if type(cell) is str:
                row[index] = cell.replace("❌", str())
    return row

while True:
    output = {"headers": get_headers(), "rows": list(), "config": {"NumberOfControlPoints": config["NumberOfControlPoints"]}}
    for concise_train_report in get_latest_concise_reports():
        row = list()
        row.append(concise_train_report["id"])
        row.append(concise_train_report["controlPoint"]["controlPointNumber"])
        row.append(concise_train_report["controlPoint"]["name"])
        if config["Datacenter"] == "bataysk":
            row.append(concise_train_report["controlPoint"]["name"].split(">")[2].split("<")[0])
        row.append(concise_train_report["startedTime"][5:10].replace("-", "."))
        row.append(concise_train_report["startedTime"][11:16])
        row.append(type_check(concise_train_report))
        row.append(concise_train_report["locomotivesCount"])
        row.append(concise_train_report["wagonsCount"])
        row.append(direction_translate(concise_train_report["direction"]))
        row.append(tgnl_check(concise_train_report))
        row += get_reports_stats(concise_train_report["id"])
        row = remove_alarms_for_noncargo(row)
        row = remove_alarms_if_tgnl_absent(row)
        row = remove_tv_alarms_for_reverse(row)
        row = remove_alarms_for_raw_trains(row, concise_train_report)
        output["rows"].append(row)
    print(output)
    data_dump(output)
    # print(debug_output)
    # data_dump(debug_output)
    time.sleep(config["RefreshInterval"]*60)