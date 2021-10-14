bufsize=1024
f = open('자켓1.jpg','rb')
h = open('자켓1_copy.jpg', 'wb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)

f.close()
h.close()
