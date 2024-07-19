from PIL import Image, ImageDraw
from PIL import  ImageFont
card = Image.new('RGB', (876, 1240), (255,255,255))
MyFont = ImageFont.truetype("MagnetTrial-Black.ttf", 20)
card.text((65, 10), text="家庭", fill =(0, 0, 0),font=MyFont)
draw = ImageDraw.Draw(card)
card.show()
card.save("result.jpg")