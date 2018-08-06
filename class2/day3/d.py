# def fn(a,b):
#     return a+b #반환
#
# rst = fn(12,21) #반환 할 경우 반환 값을 받을 변수 선언해줘야 한다.
# print(rst)

#반지름 하나를 인수로 받고 원의 면적을 반환하는 함수를 만드시요
# def circle(r):
#     return r**2*3.14
# x = circle(3)
# print(x)

# cm를 인수로 받고 인치를 반환하는 함수를 만드시요
# def cmToInch(cm):
#     return 0.393701 * cm
# inch = cmToInch(10)
# print(round(inch,2)) #round함수는 변수를 받아 소수점 표시자리 지정

# 화씨를 섭씨로 만들어주는 함수
# def fToC(f):
#     return (f-32)/1.8
# c = fToC(77)
# print(c)

#1. 반지름과 높이를 받아 원기둥의 부피를 구하는 함수
# def vol(r,h):
#     return  r**2*3.14*h
#
# rst = vol(3,10)
# print(rst)

#2. 정수 하나를 인수로 받아 해당 정수까지의 합을 반환하는 함수를 만드시오
# def sum(x):
#     for n in range(1,x):
#         x = n + x
#     return x
#
# rst = sum(10)
# print(rst)


#3. 하나의 단을 인수로 받아 해당 구구단을 출력하는 함수를 만드시오
# def gugudan(num):
#     for n in range(1,10):
#         print('%dX%d=%d'%(num,n,n*num))
# gugudan(3)

#4. 년도를 입력받아 윤년인지 아닌지 확인하시오
# def yoon(year):
#     return "윤년" if year % 4 == 0 and year % 100 != 0 or year % 400 ==0 else "윤년아님"
# rst = yoon(1904)
# print(rst)

#     if year % 4 == 0 and year % 100 != 0 or year % 400 ==0 :
#         return "윤년"
#     else:
#         return "윤년이 아니다"
# rst = yoon(1996)
# print(rst)

# 5. 키와 몸무게를 인자로 받아 비만도 결과를 표시하시오
# 표준체중(kg)=(신장(cm)-100)×0.85
# 비만도(%)=현재체중/표준체중(%)×100
# 비만도가90%이하저체중, 90초과~110% 정상,110초과~120% 과체중,120%초과 비만
# def biman(h,w):
#     std = (h - 100)*0.85
#     fat = w/std*100
#     if fat <= 90:
#         return "저체중"
#     elif 90 < fat <=110:
#         return "정상"
#     elif 110 < fat <=120:
#         return "과체중"
#     else:
#         return "비만"
# rst = biman(165,50)
# print(rst)
