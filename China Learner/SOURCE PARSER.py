import os
source = open("SOURCE1.txt", "r", encoding='UTF-8')
source = source.read()
source = source.split("\n")
result = [' ']
for Line in source:
    Entry = dict()
    SpaceSplittedLine = Line.split()
    Entry["category"] = SpaceSplittedLine[0]
    Entry["hieroglyph"] = SpaceSplittedLine[1]
    Entry["transcription"] = SpaceSplittedLine[2]
    BaseSplittedLine = Line.split(" - ")
    Entry["translation"] = BaseSplittedLine[1] 
    result.append(Entry)
print(result)    
import  json
with open('Result.json', 'w', encoding="utf-8") as fp:
    json.dump(result, fp, indent=2, ensure_ascii=False)
input()
    