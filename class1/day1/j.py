# 3항연산자 --> if문 축약형

# a = -5
# rst = 100 if a>0 else 200 #if문 우선 판단 맞으면 앞에 값 배분, 아니면 뒤에 값 배분
# print(rst)

# 하나의 정수를 읽어서 짝수면 "짝" 홀수면 "홀" 출력
#
# x = int(input("숫자를 입력하시오:"))
# rst = "짝" if x%2==0 else "홀"
# print(rst)

# 하나의 점수를 읽어 70점 이상이면 '합격' 이하면 '불합격'
# score = int(input("점수를 입력하시오:"))
# y = "합격" if score>=70 else "불합격"
# print(y)

#초단위의 시간을 받아서 몇분 몇초인지 계산하여 보자
# time = int(input("초단위 시간을 입력하시오 : "))
# min = time//60
# sec = time%60
# print(min,"분",sec,"초")

#정수 하나를 입력받았을때 절대값
# num = int(input("숫자를 입력하세요 :" ))
# abs = num if num>=0 else num*-1
# print(abs)

# 커피메뉴에 따른 매출액 계산 아메리카노 2000원 카페라떼 3000원 카푸치노 3500
# 총재료 비용이 10만원 적자일까 흑자일까 
money = 100000
ame_pri = 2000
cafe_pri = 3000
cafu_pri = 3500
ame = int(input("아메리카노 판매 개수:"))
cafe = int(input("카페라떼 판매 개수:"))
cafu = int(input("카푸치노 판매 개수:"))
sale = ame * ame_pri + cafe * cafe_pri + cafu * cafu_pri
bene = "흑자" if sale > money else "적자"
print('총매출액 : ', sale)
print(bene)
