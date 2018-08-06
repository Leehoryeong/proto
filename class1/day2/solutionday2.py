# 1. 키와 몸무게를 입력받아 비만도를 구하고 결과를 출력하시요
# 표준체중(kg)=(신장(cm)-100)×0.85
# 비만도(%)=현재체중/표준체중(%)×100
#
# 비만도가90%이하
# 저체중,
# 90초과~110%
# 정상,
# 110초과~120%
# 과체중,
# 120%초과
# 비만

height = int(input('신장:'))
weight = int(input('몸무게:'))
std = (height - 100)*0.85
fat = weight / std
if fat <= 0.9:
    print('저체중')
elif 0.9<fat<=1.1:
    print('정상')
elif 1.1<fat<=1.2:
    print('과체중')
else:
    print('비만')




# 2. 하나의 정수를 입력받아 해당 정수의 약수를 출력하시요.
num = int(input('숫자:'))
n = 1
while n<=100:
    if num%n == 0:
        print(n)
    n +=1




# 3. 하나의 정수를 입력받아 해당 정수까지의 3또는 4의 배수를
# 제외한 숫자를 출력하시요.
num = int(input('숫자:'))
for n in range(1,num+1):
    if n%3!=0 and n%4!=0:
        print(n)
    n+=1



# 4. 영한사전을 구현해 보시요
# (1-10 까지 영어 단어를 입력시 해당 숫자를 한글로 알려준다 )
# 단어를 입력하시오: one
# 하나
# 단어를 입력하시오: two
# 둘

dic = {'one':'하나', 'two':'둘', 'three':'셋', 'four':'넷', 'five':'다섯', 'six':'여섯', 'seven':'일곱', 'eight':'여덟','nine':'아홉','ten':'열'}
word = input("영단어입력:")
print(dic[word])

# 5. 연도를 입력시 해당 연도의 띠를 구하는 프로그램을 작성하시요
# ( 2018년도는 개띠임)
# 자(쥐) 축(소) 인(호랑이)묘(토끼) 진(용) 사(뱀) 오(말) 미(양) 신(원숭이) 유(닭) 술(개) 해(돼지)
year = int(input("년도입력"))
animal = ['원숭이','닭','개','돼지','쥐','소','호랑이','토끼','용','뱀','말','양']
num = year % 12
print(animal[num],'띠')

# 6. 가위, 바위, 보 게임을 작성하시요
# 예)
# 나:가위
# 결과: 나 승리 ==> 나(가위) 컴퓨터(보)
# 계속하시겠습니까(y/n)
# 나:바위
# 결과: 컴퓨터 승리 ==> 나(바위) 컴퓨터(보)
# 계속하시겠습니까(y/n)
import random
me = ['가위','바위','보']
com = ['가위','바위','보']

y=0
x = {'y':0, 'n':1}
while y < 1:
    n = random.randint(0,2)
    m = random.randint(0,2)
    if me[n] == me[0]:
        print('나',me[n],'컴퓨터:',com[m])
        if com[m] == com[0]:
            print('무승부')
        elif com[m] == com[1]:
            print('패배')
        else:
            print('승리')
    elif me[n] == me[1]:
        print('나',me[n],'컴퓨터:',com[m])
        if com[m] == com[0]:
            print('승리')
        elif com[m] == com[1]:
            print('무승부')
        else:
            print('패배')
    else:
        print('나',me[n],'컴퓨터:',com[m])
        if com[m] == com[0]:
            print('패배')
        elif com[m] == com[1]:
            print('승리')
        else:
            print('무승부')
    z=input('계속하시겠습니까?(y/n)')
    y = x[z]
print('게임을 종료합니다')


# 6. 가위, 바위, 보 게임을 작성하시요
# 예)
# 나:가위
# 결과: 나 승리 ==> 나(가위) 컴퓨터(보)
# 계속하시겠습니까(y/n)
# 나:바위
# 결과: 컴퓨터 승리 ==> 나(바위) 컴퓨터(보)
# 계속하시겠습니까(y/n)

import random #if문을 최대한 줄여보자 => Clean code
comDic={0:'가위', 1:'바위', 2:'보'}
meDic={'가위':0,'바위':1,'보':2}
result = ['비김', '컴퓨터승', '내가 이김']
com = random.randrange(3) #randint(0,3) 과 같다
print(comDic[com])
me = input('나:')
rst = (3+com - meDic[me])%3
print(result[rst])


# 7. 구구단을 다음과 같이 출력하시요
#
# 1X1=1  2X1= 2  3X1=3
# ...
# 1X9=9  2X9=18  3X9=27
#
# 4X1=1  5X1= 2  6X1=3
# ...
# 4X9=36 5X9=45  6X9=54
#
# 7X1=7  8X1=8   9X1=9
# ...
# 7X9=63 8X9=72  9X9=81
#
for m in range(2,10):
    for n in range (1,10):
        print('%dX%d=%d'%(n,m,n*m))

# 8.
# 하나의 점수를 읽어
# 90~100 'A'
# 80~89 'B'
# 70~79 'C'
# 60~69 'D'
# 나머지 'F'
# 를 딕셔너리를 이용하여 구하시요
#
# score = int(input('점수입력:'))
# board = {90<=score<100:'A', 80<=score<90:'B',70<=score<80:'C',60<=score<70:'D',score<60:'F'}
# print(board)
result = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D'}
score = int(input('점수입력:'))
print(result.get(score//10,'F'))










