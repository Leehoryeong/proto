# 람다식(임시함수) : open - closed 기법에서 불필요한 global함수의 제작을 막기 위해 사용한다
# 람다식은 역할이 끝나게 되면 증발하기 때문에 메모리를 덜 사용한다.
# 람다식은 전체적인 코드를 깔금하게 사용하도록 만들어준다.

# def hap(a,b):
#     return a+b

# rst = hap(10,20)

#람다(임시함수 or 익명함수)
hap = lambda a,b :a+b #a+b가 리턴값(return이라는 키워드 따로 없음)
print(hap(10,20))

data = [10,70,90,50,40]
data1 = [(40,50),(70,30),(20,60)] #(국어, 영어)
data2 = [{'kor':40,'eng':50},{'kor':70,'eng':30},{'kor':20,'eng':60}]

def mymax(dt,key): #dt => data, key => lambda값
    mx = None
    for n in dt:
        if mx == None or key(n) > key(mx): #open - closed 함수
            mx = n
    return mx

m = mymax(data2, lambda m:m['kor'])
print(m,m['kor'])

# m = mymax(data1, lambda m:m[1])
# print(m,m[1])

# m = mymax(data1, lambda m:m[0])
# print(m,m[0])

# m = mymax(data, lambda n:n) #lambda 함수는 역할이 끝나면 소멸한다.
# print(m)