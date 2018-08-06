# my =[10]
# a = (10,) #괄호의 의미 1. 연산자 우선순위, 2.튜블로써의 괄호 => 콤마(,)가 들어가는 순간 튜플로 인식한다.
# print(a,type(a))

# def fn(*args): #가변인자 숫자가 정해져있지 않다
#     print(args)
#
# fn(1,2,(3,4,5))
# fn((10,20,30))
# fn(*(10,20,30)) #하나의 튜플이 아닌 일반 인자처럼 인식

#가변인자를 통한 함수작성
# def circles(*rs):
#     for r in rs:
#         print(r**2*3.14)
# circles(1,2,3,4,5)


#정의되지않은 인자를 통한 딕셔너리 생성
def fn(**kwargs):  #정의되지 않은 인자 => 딕셔너리로 만들어준다.
    print(kwargs)
fn(aa=10,bb=20, cc=30)
fn(name='홍길동', age=20)
d={'name':'홍길동', 'age':20} #형식에 맞지않으면 에러발생
fn(**d) # **을 붙이면 d(딕셔너리)자체를 인식

#인자 받아오기
def fn1(a,b):
    print(a,b)
fn1(a=10,b=20)


# #딕셔너리 만들기
# data=[]
# def inputData(**kwargs):
#     data.append(kwargs)
# inputData(name='홍길동', age=20)
# inputData(name='이순신', age=30)
# inputData(name='임꺽정', age=40)
# print(data)
