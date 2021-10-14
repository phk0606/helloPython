from urllib.request import urlopen

imgurl = 'https://rooseoin.co.kr/web/product/big/202109/998c7062469b7ada043949161c897ad7.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)
