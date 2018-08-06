import random
print(random.sample([1,2,3,4,5,6],3))
s1 = '       aaa    '
print(s1.strip()) #좌우 화이트 스페이스(' ',\n,\t) 제거, 컨텐츠사이는 불가
s2 = '####aaa####'
print(s2.strip('#')) #특정문자열 제거
s3 = 'abc def ghi'
print(s3.split()) #좌우 화이트 스페이스(' ',\n,\t)를 기준으로 자른다
s4 = '010-0000-1111'
print(s4.split('-'))
