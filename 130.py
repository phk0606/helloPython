names = {'Mary':10999,'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115,'Bob':5887,'Kelly':7885}

k=input('이름을 입력하세요')
if k in names:
    print('이름 %s 수 %d' %(k, names[k]))
else:
    print('%s 없음' %k)
