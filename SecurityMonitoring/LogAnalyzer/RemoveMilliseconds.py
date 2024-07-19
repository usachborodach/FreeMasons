import os, fnmatch
LogsDir = "C:\\tmp\\antivorovator\\"

FilesList = os.listdir(LogsDir)  
for FileName in FilesList:  
    if fnmatch.fnmatch(FileName, "*.log"):
        FileContent = open(LogsDir + FileName, 'r')
        FileContent = FileContent.read()
        FileContent = FileContent.split("\n")
        for Item in FileContent:
            Index = FileContent.index(Item)
            Item = Item[:17] + Item[24:]
            FileContent[Index] = Item
    f = open(LogsDir + "processed_" + FileName, 'w')
    #print(FileContent, file=f, sep="\n")
    for item in FileContent:
        print(item, file=f)    
    f.close()