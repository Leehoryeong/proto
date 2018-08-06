# data = [10,20,30,40,50]
# print(200 in data) # in 연산자 data안에 값이 있으면 True 없으면 False
# print(200 not in data) #not in 연산자 data안에 값이 없으면 True 있으면 False
# s="Hello Python"
# print("Py" in s) #문자열도 in연산자 사용가능
# dic = {'aa':10, 'bb':20, 'cc':30}
# print('aa' in dic)
# print(10 in dic.values()) #in 연산자는 딕셔너리에서 key값의 존재여부만 판단가능하다.
#dic.values = [10,20,30]


#'철'자가 있는 이름만 리스트로 구성하시오
names = ['이순신', '홍길동', '김철수1', '김철수2']
name = [n for n in names if '철' in n]
# name = (n for n in names if '철' in n)
print(name)
# print(next(name))
