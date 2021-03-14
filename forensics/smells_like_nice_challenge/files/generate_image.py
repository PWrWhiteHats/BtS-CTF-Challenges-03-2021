from PIL import Image, ImageDraw, ImageFont
import dotenv

dotenv.load('resources/challenge.env')

FLAG = dotenv.get('FLAG') or "fake{fl4gs_4r3_dumb}"
FLAG_IMAGE_FILE = dotenv.get('FLAG_IMAGE_FILE') or 'flag.png'
IMG_WIDTH = 320
IMG_HEIGTH = 240
FLAG_WDTH_START = 30
FLAG_HGTH_START = 120
FONT_SIZE = 30

# Create flag image
img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGTH), color = (250, 10, 10))
fnt = ImageFont.truetype('resources/comic.ttf', FONT_SIZE)
draw = ImageDraw.Draw(img)
if FLAG_WDTH_START + len(FLAG)*FONT_SIZE/2 > IMG_WIDTH - FLAG_WDTH_START:
    mid = (len(FLAG)+1)//2
    if FLAG_WDTH_START + mid*FONT_SIZE/2 > IMG_WIDTH - FLAG_WDTH_START:
        print("Cannot draw flag - text too long")
        exit(1)
    else:
        print("Flag too long but can be fit - splitting in half")
        first = FLAG[:mid]
        print(f"First half: {first}")
        second = FLAG[mid:]
        print(f"Second half: {second}")
        draw.text((FLAG_WDTH_START,FLAG_HGTH_START), first, font=fnt, fill=(0, 0, 0))
        draw.text((FLAG_WDTH_START,FLAG_HGTH_START + FONT_SIZE + 1), second, font=fnt, fill=(0, 0, 0))
else:   
    draw.text((FLAG_WDTH_START,FLAG_HGTH_START), FLAG, font=fnt, fill=(0, 0, 0))
img.save(FLAG_IMAGE_FILE)
print(f"Saved image \"{FLAG_IMAGE_FILE}\" with flag \"{FLAG}\"")