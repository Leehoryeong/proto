# if n<5: #조건이 False면 출력되지 않는다.
#     print('n=', n)
#     n+=1
# 반복문 while
# n = 0
# while n<5: #while 옆 조건이 False가 될때까지 반복
#     if n==3:
#         break #break는 조건이 만족하면 반복문을 탈출시켜준다.
#     print('n=',n)
#     n+=1
# print('hello')

#1+2+..+10

n = 1
nsum=0
while n<=10:
    print('n=',n)
    nsum = nsum + n
    n+=1 # n = n+1
print('nsum=',nsum)
