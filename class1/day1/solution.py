# 1. 다음을 구하시요
# 1) kg을 입력받아 근으로 변환하시요
# kg = int(input("kg입력 : "))
# geun = 1.666667 * kg
# print(kg,"kg은",geun,"근입니다")

# 2) m 를 입력받아 마일로 변환하시요
# m = int(input("미터입력 : "))
# mile = 0.000621371 * m
# print(m,"m는",mile,"마일입니다")

# 3) 화씨 를 입력받아 도로 변환하시요
# f = int(input("화씨입력 : "))
# c = (f - 32)/1.8
# print("화씨",f,"도 는","섭씨",c,"도입니다")




# 2. 다음 도형의 부피를 구하시요
# 1) 반지름과 높이를 입력받아 원기둥의 부피
# r = int(input("반지름 입력:"))
# h = int(input("높이 입력:"))
# pie = 3.14
# vol = r**2*pie*h
# print(vol)

# 2) 반지름과 높이를 입력받아 원뿔의 부피
# r = int(input("반지름 입력:"))
# h = int(input("높이 입력:"))
# pie = 3.14
# vol = r**2*pie*h/3
# print(vol)


# 3) 가로, 세로 높이를 입력받아 사각기둥의 부피
# h = int(input("가로길이 입력:"))
# v = int(input("세로길이 입력:"))
# height = int(input("높이 입력:"))
# vol = v*h*height
# print(vol)


# 3. 년도 입력받아
# 1) 윤년여부를 출력하시요
# 윤년의 조건
# 1-1) 4로 나눠 떨어지지만 100으로 나눠 떨어지지 않아야 한다 또는
# 1-2) 400 으로 나눠 떨어지면 윤년임
# year = int(input("년도를 입력하세요:"))
# check = "윤년입니다" if year % 4 ==0 and year % 100 != 0 or year % 400==0 else "윤년이 아닙니다"
# print(check)

# 2) 나이를 출력하시요
# year = int(input("년도를 입력하세요:"))
# age = 2018 - year + 1
# print(age)





# 4. 상품가격과 지불액을 입력받아
# 거스름돈을 최소화 하도록 하시요
# (거스름돈 500, 100, 50, 10 원)
# 예) 상품가격 1230, 지불액 2000원이면
# 거스름돈 500원 1개, 100원 2개,
# 50원1개 10원 2개)
# price = int(input("상품가격을 입력하세요:"))
# money = int(input("지불액을 입력하세요:"))
# change = money-price
# M500 = change // 500
# change = change % 500
#
# M100 = change // 100
# change = change % 100
#
# M50 = change // 50
# change = change % 50
#
# M10 = change // 10
#
# print(M500, M100, M50, M10)

# 5. 원금이 1000만원이고
# 매달 이자율 2% 를 1년간 예치했을때
# 만기금은 얼마인가?
# (단리계산, 복리계산 각각 구하시요)
# origin  = int(input("원금을 입력하세요(만원단위): "))
# 복리 = origin*(1.02**12)
# 단리 = origin+1000*0.02*12
# print(복리,"만원", 단리,"만원")
