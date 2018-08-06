#내장 라이브러리(builtins) => print, input 등
#제공 라이브러리
#서드파티(설치)

# import mymodule #import했을때 확장자가 py,pyc,pyd 여야 한다.
# import mymodule as m #불러오는 파일을 약어로 사용
from mymodule import * #마이모듈에서 함수 모두를 꺼내 오겠다 (바로사용가능), mymodule에 있는 코드를 모두 실행한뒤에 usemodule실행
#mymodule에서 지정된 print(__name__)이 usemodule에서는 mymodule로 출력된다.
def main():
    print('usemodule...',__name__) #__name__에 __main__이라는 변수가 들어있다.
    rst = hap(10,20)
    print(rst)
    rst = gop(10,20)
    print(rst)

if __name__ == '__main__':
    main()


# import sys
# sys.path.append("C:\mylib") #import를 통해 새롭게 읽어올수 있는 주소 추가
# print(sys.path) #파이썬패쓰 저장된 위치확인
# python -m py_compile module.py ==> mymodule.pyc
