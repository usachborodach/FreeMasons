#A4 = 297x210mm
#Разрешение = 300dpi
#A4 = 2480x3508px
#Карточки = 4x2шт
#Карточка = 877x1240px

# ЗАДАЧИ
#запаковать это дело в функцию и нагенерить итерируя data
#добавить рамочку для вырезания
#собрать по 8 карточек на лист а4
import json
from PIL import Image, ImageDraw, ImageFont
def CreateCard(TranscriptionText, GlyphText, TranslationText):
    TranscriptionSize = 200
    TranscriptionX = 40
    TranscriptionY = 40
    GliphSize = 400 # ДЛЯ ДВУХ СИМВЛОВ! ДЛЯ ТРЁХ НАДО СТАВИТЬ МЕНЬШЕ!
    GliphX = 40
    GliphY = 440
    TranslationSize = 100
    TranslationX = 40
    TranslationY = 1000
    Card = Image.new('RGB', (877, 1240), (255,255,255))
    Draw = ImageDraw.Draw(Card)
    Draw.rectangle([(3, 3), (874, 1237)], outline ="red") 
    MyFont = ImageFont.truetype('simsun.ttc', TranscriptionSize)
    Draw.text((TranscriptionX, TranscriptionY), text=TranscriptionText, fill =(0, 0, 0),font=MyFont)
    MyFont = ImageFont.truetype('simsun.ttc', GliphSize)
    Draw.text((GliphX, GliphY), text=GlyphText, fill =(0, 0, 0),font=MyFont)
    MyFont = ImageFont.truetype('arial.ttf', TranslationSize)
    Draw.text((TranslationX, TranslationY), text=TranslationText, fill =(0, 0, 0),font=MyFont)
    Card.save("cards\\"+TranslationText+".jpg")

Data = json.loads(open("data.json", encoding="utf-8").read())
for Item in Data:
    if Item["category"] == "СЕМЬЯ":
        CreateCard(Item["transcription"], Item["hieroglyph"], Item["translation"])
print("done")