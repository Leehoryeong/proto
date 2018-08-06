# 함수 설계 윈칙
# 1. SRP(단일책임) : 하나의 함수는 2가지 이상의 기능을 하면 안된다
# - 유지보수를 용이하게 하기 위해 최소의 기능으로 쪼개준다.
# 2. Open - Closed (개방 - 폐쇄) : 기존 코드 수정에는 Closed 기능확장에는 Open
# - 파이썬 데이터 처리 라이브러리는 open-closed로 만들어져있다. C#(LinQ)

data = [10,70,90,50,40]
data1 = [(40,50),(70,30),(20,60)] #(국어, 영어)
data2 = [{'kor':40,'eng':50},{'kor':70,'eng':30},{'kor':20,'eng':60}]
def mymax(dt):
    mx = None
    for n in dt:
        # if mx == None or n>mx: #단순리스트 크기비교
        # if mx == None or n[0]>mx[0]: #리스트안의 튜플구조 크기비교(기준 : 앞에 수)
        if mx == None or n['kor']>mx['kor']: #리스트안의 딕셔너리구조 크기비교(기준 : 'kor')
            #자료가 어떤구조를 갖는지에 따라서 전부 따로 설정해주어야 하는 불편함이 있다.
            mx = n
    return mx

m = mymax(data2)
print(m,m['kor'])
