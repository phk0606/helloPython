class MyClass:
    def __init__(self, txt):
        self.var =txt
        print('MyClass 인스턴스 객체가 생성되었습니다.')
        print('생성자 인자로 전달받은 값은 <' + self.var +'> 입니다.')

obj = MyClass('영희')
print(obj.var)
