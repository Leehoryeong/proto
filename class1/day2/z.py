#함수 range(시작값, 끝값, 증가치) ==> 리스트 만들어준다
# 시작값<= 리스트 < 끝값
# r = range(1,11,2) #시작값, 증가치 생략가능 => 디폴트값 시작값 0 증가치 1 (끝값은 생략불가)
# print(list(r))
# r = range(11)
# print(list(r))
#
# for n in range (1,5): # [1,2,3,4] 입력한것과 똑같음
#     print(n)
# nsum = 0
# for n in range(1,11):
#     print("n=",n)
#     nsum = nsum + n
# print('nsum=',nsum)

# for n in range(2,11,2):
#     print("n=",n)

# for n in range(1,11):
#     if n%2==0:
#         print("n=",n)

# 1~10까지 3의 배수를 제외한 숫자를 출력하시오
# 1 2 4 5 7 8 10
# for n in range(1,11):
#     if n%3 != 0:
#         print(n)

# for n in range(1,4):
#     for m in range(1,4):
#         print(n,m)

# 구구단 출력
for n in range (2,10):
    for m in range(1,10):
        # print(n,'X',m,'=',n*m)
        print('%dX%d=%2d'%(n,m,n*m))
