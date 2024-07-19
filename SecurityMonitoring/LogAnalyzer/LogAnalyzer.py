import os, fnmatch, pprint
from datetime import datetime
import matplotlib.pyplot as plt

LogsDir = "C:\\tmp\\antivorovator\\"

FilesList = os.listdir(LogsDir)  
for FileName in FilesList:  
    x = []
    y = []
    fig = plt.figure()
    if fnmatch.fnmatch(FileName, "*.log"):
        FileContent = open(LogsDir + FileName, 'r')
        FileContent = FileContent.read()
        FileContent = FileContent.split("\n")
        for Item in FileContent:
            if Item.find(" SecurityChannelState: ") > -1:
                Item = Item.split(" SecurityChannelState: ")
                FormatedDate = datetime.strptime(Item[0], "%Y-%m-%d %H:%M:%S")
                x.append(FormatedDate)
                y.append(Item[1])
    plt.plot(x, y, label = FileName)
    plt.legend(fontsize=14)
    plt.tight_layout()
    fig.savefig(FileName + '.png')

#pretty_print_json = pprint.pformat(AllTheLogs)
#pretty_print_json = pretty_print_json.replace("\'", "\"")
#with open("result.json", 'w') as f:
#    f.write(pretty_print_json)
