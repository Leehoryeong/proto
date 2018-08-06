# 실행중에 발생하는 오류 예외처리
# 파이썬에서 알려진 오류는 자동 처리

def div(a,b):
    return a/b
data = [10,20,30,40]
# data[5] = 100
# print(data) #에러가 발생해서 프로그램이 종료 된다.

try:
    n = input('숫자입력:') #숫자가 아닌값 입력할때 오류 판별
    n = int(n)
    print(n)
except Exception as err:
    print("숫자로 정확하게 입력하세요")

try:
    fp = open('test.txt;,'r'')
    rd = fp.read()
    fp.close()
except  Exception as err:\
    print("파일이 없습니다..")


# try:  #try문을 통해서 에러를 자동으로 처리해준다
    # data[5] = 100
    # rst = div(10,0) #15 나누기 0을 실행 할 수 없기때문에 에러발생 => 값을 err로 보내준다.
    # print(data)
#   except Exception as err:
#     print("에러:", err)
print('hello')
