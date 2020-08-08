from PIL import Image, ImageFont, ImageDraw
import requests

result = requests.get('https://graviex.net/api/v2/tickers',verify=False) #api
return_dict = dict()
return_dict["tickets"] = list()
result_d = dict()
for i in result.json():
    if i[-3:] =='btc': #проверка окончания пары BTC
        data = result.json()[i]
        ticker = data['ticker']
        name = i[:-3]
        change = round(float(ticker['change']),1)
        if change > 0:
            change = '+' + str(change)
        else:
            change = str(change)
        img = Image.open('coin-info.png')  # оригинал изображения который лежит в корне
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("tahoma.ttf", 29)  # шрифт и размер
        fnt2 = ImageFont.truetype("tahoma-bold.ttf", 35)
        d.text((30, 60), 'TIKER: ', font=fnt, fill=(0, 0, 0, 0))  # позиция
        d.text((125, 55), name.upper(), font=fnt2, fill=(0, 0, 0, 0))  # позиция
        d.text((30, 120), 'BUY: ', font=fnt, fill=(0, 0, 0, 0))
        d.text((100, 115), ticker['buy'], font=fnt2, fill=(0, 0, 0, 0))
        d.text((30, 180), 'SELL: ', font=fnt, fill=(0, 0, 0, 0))
        d.text((105, 175),ticker['sell'], font=fnt2, fill=(0, 0, 0, 0))
        d.text((30, 240), 'VOLBTC: ', font=fnt, fill=(0, 0, 0, 0))
        d.text((145, 235),str(ticker['volbtc']), font=fnt2, fill=(0, 0, 0, 0))
        d.text((30, 300), 'CHANGE: ', font=fnt, fill=(0, 0, 0, 0))
        d.text((150, 295),change, font=fnt2, fill=(0, 0, 0, 0))
        img.save("img_done/" + i + ".png", "PNG")  # куда сохранять
        del d