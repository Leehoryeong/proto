# def fn(): #패킹발생
#     return 10,20
# rst = fn()
# print(rst)
# a,b = fn()
# print(a,b)


# def shape(r,h,w):
#     return r**2*3.14, h*w #패킹발생
# rst = shape(3,10,20)
# print(rst)
#
# circle, rect = shape(3,10,20)
# print(circle,rect)

# def fn1(a,b):
#     print(a,b)
# fn1(100,200)
# fn1(b=1000, a=2000) #명시적 인자 호출
# fn1() #인자가 없기 때문에 오류가 난다

# def fn2(a=10, b=20, c=30): #디폴트인자
#     print(a,b,c)
# print(10,20,30,sep='-') #파이썬에서 기본적으로 제공되는 함수의 기본인자(sep, end)를 바꾸어준다
# print('abc', end=' ')
# print('def')

# def fn3(*args): #가변인자(인자의 갯수가 정해져있지 않다)
#     print(args)
#     for n in args:
#         print(n)
# fn3(10,20,30,40,50)
# fn3('aa','bb','cc')


#코드작성 -> 컴파일러 -> 0,1 2진법 변환 -> 프로세스 실행 ->


# fn2()
# fn2(100) #a인자에 100이 들어가고 나머지는 디폴트 값
# fn2(100,200) #a 100, b 200, c기본값
# fn2(100,200,300) #a 100, b 200, c 300
# fn2(b=200) #b 200 나머지 기본값
