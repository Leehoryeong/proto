data = [10,70,90,50,40]
data1 = [(40,50),(70,30),(20,60)] #(국어, 영어)
data2 = [{'kor':40,'eng':50},{'kor':70,'eng':30},{'kor':20,'eng':60}]

#함수 sum
rst = sum(data) #sum은 lambda식이 없다. => iterable 복합데이터 타입만 사용가능
print(rst)

# rst = sum(data1) #리스트 - 튜플 형태는 계산이 불가능하다
d = [n[0] for n in data1]
rst = sum(d)
print(rst)
rst = sum(map(lambda n:n[0], data1))
print(rst)
print(sum([n['kor'] for n in data2]))
