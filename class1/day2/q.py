# 복합데이터타입(시퀀스, iterable) : 문자열, 리스트[ ], 튜플( )
# 문자열
# a,b,c = 10,20,30
# print(a,b,c)

#변경불가능(immutable) : 문자열, 튜플(함수, 반복문)
#변경가능(mutable) : 리스트

#튜플
t = (10,20,30)
# t[0] = 100 # 수정이 안된다
print(t.index(20))
print(t.count(20))
print(t,type(t))
print(t[0])

#패킹과 언패킹
a,b,c = (100, 200, 300) #이런식으로 입력하면 파이썬이 자동으로 괄호를 없앰 => unpacking 각각 a,b,c에 값 지정
print(a,b,c)
d,e,f = [1000, 2000, 3000] #리스트도 unpacking 마찬가지
print(d,e,f)

myT = 1,2,3 #packing 자동으로 괄호를 붙인다 => 튜블로 자동변환
print(myT)
