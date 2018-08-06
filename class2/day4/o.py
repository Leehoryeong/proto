#일급함수(c언어,c++ (함수포인터), java,c#(delegate) : 람다식(javascript))
#함수 : 할당, 인수, 리턴, 함수안에 함수 포함

# fn() # 6601296 --> 주소로 이동 해서 실행한 이후에 다음라인으로 이동
# fn()
# print(id(fn))
# my = fn #shallow copy 주소만 카피
# print(id(my))
# my()


def fn():
    print('fn call')

def fn1(aa):
    aa()

def fn2():
    return fn

rst = fn2()
rst() #fn2 실행 => fn값 반환 
