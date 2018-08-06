# 내장 리스트
# myList = [n * 10 for n in range(1,6) if n%2==0] #if문이 True인 경우에만 n값 대입
# print(myList)

# data = [100,200,300,400]
# d = [n-10 for n in data if n>200]
# print(d)

# # 10의 약수를 내장리스트를 이용해 구해보자
# n10 = [n for n in range(1,11) if 10%n==0]
# print(n10)

#세금 3.3을 제한 실수령액을 구하시오
import sys
salary = [1000,2000,3000,4000]
realPay = (n*0.967 for n in salary) # generator => generator의 생성은 내장리스트와 함수 yield를 이용해서 만든다
# realPay = [n*0.967 for n in salary] #lsit
print(sys.getsizeof(realPay)) #realPay를 담고 있는 메모리의 크기를 보여준다 => 값이 증가할수록 데이터크기 증가
#generator는 메모리를 잡지 않고 next 함수를 통해 하나씩 결과 값만 얻는다. 
# realPay = {n*0.967 for n in salary} #set
print(realPay)  #그때 그때 연산한 값을 반환, 메모리 사이즈가 증가하지 않는다, 데이터 수가 어마어마하게 많은경우 사용(빅데이터)
print(list(realPay)) # [next(realPay),next(realPay),next(realPay),next(realPay)]
# for d in realPay: #d = next(realPay),d = next(realPay),d = next(realPay),d = next(realPay) 후에 for루프에서 빠져나간다
#     print(d)
# print(next(realPay))
# print(next(realPay))
# print(next(realPay))
# print(next(realPay))
# print(next(realPay)) # 계산할 데이터가 더 이상 없는 경우 stopiteration 오류발생
# data = [('aaa',10),('bbb',20),('ccc',30)]
# d = {k:v for k,v in data}  #unpacking이 이루어지고 dict로 구성된다.
# print(d)
