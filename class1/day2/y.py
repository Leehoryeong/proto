# for변수 in 복합데이터 타입 (문자열, 리스트, 튜플, 세트, 딕셔너리):
s = 'abcdef'
myList = [10,20,30,40]
myT = (100,200,300)
myD = {'aa':10,'bb':20, 'cc':30}
# for n in s: #n = s[0] s[1] s[2] .. s[5] 문자열 s의 갯수만큼
#     print(n)
# for n in myList:
#     print(n)
# for n in myT:
#     print(n)
# for n in myD:
#     print(n)
# for n in myD.keys():
#     print(n)
# for n in myD.values():
#     print(n)
for n in myD.items(): #튜플형식으로 글자반환
    print(n)
for k,v in myD.items(): #언패킹 되어 k,v에 값이 자동으로 들어간다
    print(k,v)
