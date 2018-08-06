import random
# n = random.randint(1,5) #1~5까지 임의의 숫자를 반환
# print("n=", n)
coin = random.randrange(2) # 0<= n <2 까지 임의의 숫자를 반환
print("동전 던지기 게임을 시작합니다.")

# sol1)
if coin ==0 :
    print("앞면입니다")
else:
    print("뒷면입니다.")
print("게임종료")

# sol2)
print(["앞면이 나왔습니다.","뒷면이 나왔습니다."][coin])
print("게임을 종료합니다.")
