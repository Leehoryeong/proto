#
# # 1. 다음을 함수로 만들고 호출하여 결과를 출력하시요
# # 1) 하나의 정수를 인수로받아 해당 정수의 소수(prime number)를 반환한다
# def number(num):
#     a =[n for n in range(1,num+1) if num%n ==0]
#     if len(a) <=2 :
#         return num
# x = int(input("정수를 입력하세요:"))
# print(number(x))
#
# # 2) 하나의 연도를 입력받아 해당연도의 띠를 반환한다
# # 자(쥐) 축(소) 인(호랑이)묘(토끼) 진(용) 사(뱀) 오(말) 미(양) 신(원숭이) 유(닭) 술(개) 해(돼지)
#
#
#
# def ganji12(year):
#     animal = ['원숭이','닭','개','돼지','쥐','소','호랑이','토끼','용','뱀','말','양']
#     num = year % 12
#     return animal[num]
#
# rst = int(input("년도입력:"))
# print(ganji12(rst),'띠')
#
#
# # 3) grade=[ 90,50,60,20,40,70, 60] 이 있을때
# # grade 를 인자로 받아 30 보다 큰수를 반환하는 함수를 만드시요
# grade=[90,50,60,20,40,70, 60]
# def large(x):
#    y = [n for n in x if n>30]
#    return y
# print(large(grade))
#
#
# # 2. 다음을 작성하시요
# # ( 단 입력함수, 출력함수를 만들어서
# #  작성하여야한다)
# # 이름:
# # 나이:
# # 계속입력하시겠습니까(y/n)?
# # n입력시
# # =============================
# # 	이름	나이
# # =============================
# # 	xxx	xx
# # 	xxx	xx
# # ....
# #데이터 저장 방법
# #1. 리스트 튜플(리스트)
# #2. 리스트 딕셔너리
data = [] #비어있는 리스트
def inputData():
    while True:
        name = input("이름:")
        age = input('나이:')
        yn = input('계속입력하시겠습니까?')
        data.append({'name':name,'age':age})
        if yn =='n':
            break
def outData():
    print("="*30)
    print('%10s%10s'%('이름','나이'))
    print("="*30)
    for d in data:
        print('%(name)10s%(age)10s'%d)

# inputData()
# outData()

# # s3 = 'abc def ghi'
# # print(s3.split()) #좌우 화이트 스페이스(' ',\n,\t)를 기준으로 자른다
# # s4 = '010-0000-1111'
# # print(s4.split('-'))
# # 3. 로또 프로그램을 작성하시요
# # 1~45개중 6개를 선택 했을때 맞은 갯수를 출력한다
#
#
# c = int(input("1.게임시작 2.게임종료:"))
# y=0
# x = {'y':0, 'n':1}
# if c == 1:
#     while y < 1:
#         myNum = input('6개숫자를 입력하세요:')
#         mNum = myNum.split( )
#         clear = [int(mNum[n]) for n in range(0,len(mNum))]
#         import random
#         def lotto(cong):
#             allNum = [n for n in range(1,46)]
#             luckyNum = random.sample(allNum,6)
#             print(luckyNum)
#             lucky = [n for n in luckyNum if n in cong ]
#             return len(lucky)
#         print(lotto(clear),'개 맞았습니다')
#         z=input('계속하시겠습니까?(y/n)')
#         y = x[z]
# print('게임을 종료합니다')

import random
luckyNum=random.sample([n for n in range(1,46)],6)
# print(luckyNum)
meIn = input('6개의숫자입력:')
meIn = [int(n) for n in meIn.split()]
# print(meIn)
collect = [n for n in meIn if n in luckyNum ]
print(collect,'정답의개수',len(collect))


#
#
#
#
#
# # 메뉴)
# # 1. 게임시작
# # 2. 종료
# #
# # 1~45개 중 중복되지 않게 1~6개의 숫자를 스페이로 구분
# # 하여 입력하시요:1 7 13 19 45
# # 2개를 맞았습니다. 예) 랜덤 6개가  1, 2, 5, 7, 11, 40 이면
# # 계속하시겠습니까(y/n):
# #
