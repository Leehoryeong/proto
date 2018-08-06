# num =-3
# if num>0:
#     print("양수입니다.")
# elif num==0:  #elif 갯수 제한 없음
#     print('0입니다.')
# else:
#     print('음수입니다.')
# print('Hello')

#하나의 점수를 읽어 90~100 : 'A', 80~89 : B', 70~79 : 'C', 60~69 : 'D', 나머지 'F'

# score = int(input("점수를 입력하세요 : "))
# if 0<= score <= 100:
#     if score >= 90:
#         print('A')
#     elif score>=80:
#         print('B')
#     elif score>=70:
#         print('C')
#     elif score>=60:
#         print('D')
#     else:
#         print('F')
# else:
#     print("점수입력이 잘못됨")
#
time = int(input("시간을 입력 : "))
weather = input("날씨를 입력 : ")
if 6<=time <9 and weather=="맑음":
    print('운다')
else:
    print('안운다')
