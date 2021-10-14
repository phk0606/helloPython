from os.path import getsize

file1='stockcode.txt'
file2='e:/pythonEx/자켓1.jpg'
file_size1=getsize(file1)
file_size2=getsize(file2)

print('파일명: %s \t파일 크기: %d' %(file1, file_size1))
print('파일명: %s \t파일 크기: %d' %(file2, file_size2))
