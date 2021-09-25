val = input('문자 코드값 입력')
val = int(val)
try:
    ch=chr(val)
    print('코드값:%d[%s],문자:%s'%(val,hex(val), ch))
except ValueError:
    print('입력한 %d에 대한 문자 없음'%val)
