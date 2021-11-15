from PIL import Image, ImageDraw, ImageFont
import pandas as pd
df = pd.read_csv('na.csv')

# font = ImageFont.truetype('PTF75F.ttf',95)

for index,j in df.iterrows():
    img = Image.open('game.png')

    font = ImageFont.truetype('Lato-Bold.ttf',100)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1000,680),text='{}'.format(j['name']),fill=('black'),font=font, anchor="ms")

    # font2 = ImageFont.truetype('Montserrat-Medium.ttf',100)
    # draw = ImageDraw.Draw(img)
    # draw.text(xy=(1000,1000),text='{}'.format(j['id']),fill=('black'),font=font2, anchor="ms")

    img.save('image/{}.png'.format(j['name']))







# CULTURAL CLUB
# from PIL import Image, ImageDraw, ImageFont
# import pandas as pd
# import os
# df = pd.read_csv('naam.csv')
# font = ImageFont.truetype('PTF56F.ttf',147)
# for index,j in df.iterrows():
#     img = Image.open('cultural.png')
#     draw = ImageDraw.Draw(img)
#     draw.text(xy=(998,710),text='{}'.format(j['name']),fill=('#383639'),font=font, anchor="ms")
#     img.save('image/{}.png'.format(j['name']))