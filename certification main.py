from PIL import Image, ImageDraw, ImageFont
import pandas as pd
df = pd.read_csv('na.csv')

# font = ImageFont.truetype('PTF75F.ttf',95)

for index,j in df.iterrows():
    img = Image.open('platinum_mockup/platinum_certificate.jpg')

    font = ImageFont.truetype('platinum_mockup/certificate_name_font.ttf', 143)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(923,655),text='{}'.format(j['name']),fill=('#F2D770'),font=font, anchor="ms")

    # font2 = ImageFont.truetype('Montserrat-Medium.ttf',100)
    # draw = ImageDraw.Draw(img)
    # draw.text(xy=(1000,1000),text='{}'.format(j['id']),fill=('black'),font=font2, anchor="ms")

    img.save('image/{}.png'.format(j['name']))






for index,j in df.iterrows():
    img = Image.open('platinum_mockup/card mockup-01.jpg')

    font = ImageFont.truetype('platinum_mockup/Poppins-Bold.ttf', 125)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(2625,765),text='{}'.format(j['name']),fill=('#080D44'),font=font, stroke_width=1, anchor="rs")

    font2 = ImageFont.truetype('platinum_mockup/Poppins-Regular.ttf',67)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1790,1390),text='{}'.format(j['id']),fill=('black'),font=font2, anchor="ls")

    img.save('m_card/{}.png'.format(j['name']))







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