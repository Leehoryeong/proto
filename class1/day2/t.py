# 2차원데이터구조
data = [[100,70], [60,50], [40,80]]
print(data[0][0])
print(data[1][1])
print(data[2][0])
k, e = data[1] #언패킹 발생
print(k,e)
data1 = [{'kor':100,'eng':70},{'kor':100,'eng':70},{'kor':100,'eng':70}]
print(data1[0]['kor'])
print(data1[1]['eng'])

# a = 10
# s1 = 'a=%d' %a
# print(s1)
# aa = 10
# bb = 3.14
# cc ='abc'
# s2 = 'aa=%d bb=%.2f cc=%s' %(aa,bb,cc)
# print(s2)

d = {'name':'홍길동','kor':100,'eng':70}
s = '이름:%(name)s 국어:%(kor)d 영어:%(eng)d' %d  #딕셔너리 포맷
print(s)
