from PIL import Image, ImageDraw, ImageFont
import pandas as pd
df = pd.read_csv('na.csv')

# font = ImageFont.truetype('PTF75F.ttf',95)

for index,j in df.iterrows():
    img = Image.open('game.png')

    font = ImageFont.truetype('Lato-Bold.ttf',100)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1000,680),text='{}'.format(j['name']),fill=('black'),font=font, anchor="ms")

    font2 = ImageFont.truetype('Montserrat-Medium.ttf',100)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1000,1000),text='{}'.format(j['id']),fill=('black'),font=font2, anchor="ms")

    img.save('image/{}.png'.format(j['name']))
