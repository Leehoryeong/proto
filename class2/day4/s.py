data = [10,70,90,50,40]
data1 = [(40,50),(70,30),(20,60)] #(국어, 영어)
data2 = [{'kor':40,'eng':50},{'kor':70,'eng':30},{'kor':20,'eng':60}]
data3 = ['홍길동', '이순신', '김철수1', '김철수2']
data4 = [1000, 7000, 9000, 5000, 4000]
# 이름에 철이 들어가는 데이터 반환
f = filter(lambda n:'철' in n, data3)
print(list(f))


#기본 내장함수 : max, min, filter, map, sorted,sum



# 필터함수
# f = filter(lambda n:n>=50,data) #generator 표시됨 , 메모리를 차지하지 않고 그때그때 꺼내서 계산, 조건이 True인것만 보여줌
# print(f)
# print(list(f))


# def myfilter(key,dt):
#     return (n for n in dt if key(n))
# f = myfilter(lambda n:n>=50,data)
# print(f)
# print(list(f))  #generator 값은 리스트화 시켜주자!


#함수 map : 개별데이터 연산
# m = map(lambda n:n+2,data)
# print(list(m))

# data4의 연봉데이터를 세금 3.3%를 제한 실수령액
# def mymap(key,data):
#     return [key(n) for n in data]
# m = mymap(lambda n:n+2, data)
# print(m)

# pay = map(lambda n:n*(1-0.033),data4)
# print(list(pay))

# m = map(lambda n:n[0], data1)
# print(list(m))

# m = map(lambda n:n['kor'],data2)
# print(list(m))


#정렬함수
# s = sorted(data) #원본데이터를 오름차순 정렬된 데이터화
# print(s)
# s = sorted(data1, key = lambda n:n[0], reverse=True) #국어점수가 낮은거에서 높은거로 내림차순 정렬
# print(s)
# s = sorted(data2, key = lambda n:n['kor']) #국어점수 오름차순
# print(s)


# data.sort()
# print(data)


# for n in f:  #next(f), next(f), next(f)
#     print(n)
# print(next(f))

# m = min(data1, key = lambda n:n[0]) #내장함수 min
# print(m)
# m = max(data) #내장함수 max 만들어진 방식에 따라 사용하면 된다.
# print(m)
# m = max(data1, key= lambda n:n[0]) #key= 을 명시해주지 lambda식이 않으면 인식하지 못한다
# print(m,m[0])
# m = max(data1, key= lambda n:n[1])
# print(m,m[1])
# m = max(data2, key= lambda n:n['kor'])['kor']
# print(m)
