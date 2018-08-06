# a = 5
# if a>0 :
#     print('크다')
# else:
#     print('아니다')
#
# print('hello')

# 하나의 정수를 입력받아 3의 배수이면 3의배수임 아니면 아님을 출력하시오
# x = int(input("정수를 입력하세요:"))
# if x%3==0:
#     print("3의 배수이다")
# else:
#     print("3의배수가 아니다")

a= False +1
print(a) #파이썬에서 True는 1 False는 0으로 본다

# n = 5
# rst = [100,200][n>0] #인덱스가 True값이기 때문에 1자리에 있는 값이 입력 된다.
# print(rst)

# 하나의 정수를 입력받아 짝수면 '짝' 홀수면 '홀' 출력
num = int(input('정수를 입력하세요 :'))
# rst = ('짝','홀')[num%2]
rst = ({0:'짝',1:'홀'})[num%2]
print(rst)

n=5
rst = {True:100, False:200}[n>0]
print(rst)
