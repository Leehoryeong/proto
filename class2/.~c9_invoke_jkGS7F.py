#컴파일 되어 있는 내장 변수 및 함수 및 클래스
# __name__ = '__main__' #기본적으로 생성되는 전역변수
# __doc__ = None
# ...

g = 10
def fn():
    global g #전역변수를 생성
    g=100
    print(locals()) #지역변수 목록 => 함수 안쪽에서 찍어봐야한다.
fn()
print(g)
print(__file__)
# print(globals())
