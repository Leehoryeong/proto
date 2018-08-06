#객체 : 속성, 메소드
#객체.속성
#객체.메소드()

# slist = ['국어', '영어', '수학', '과학'] #mutable
# slist는 list객체
# slist.append('생물') #마지막에 데이터 추가
# slist.append('물리')
# slist.insert(1, '한문') #인덱싱 1번자리에 한문 추가
# slist.remove('영어') #영어라는 데이터 삭제
# slist.pop(2) #인덱스 2번자리에 있는 데이터 삭제
# print(slist.index('영어')) #영어라는 데이터가 인덱스 어디위치에 있는가?
# slist[1] = '영어1' #데이터 수정
# slist.sort( reverse= True) #데이터의 오름차순 정렬(reverse는 내림차순)
# print(len(slist))
# print(slist)

# print(slist,type(slist))
# print(slist[0],slist[-1])
# nlist = [10,20,30,40,50]
# print(nlist)
# print(nlist[0])
# print(nlist[1:4:1]) # 1<= nlist < 4 , 1,2,3

#제일 친한 친구 5명의 이름을 리스트에 저장했다가 출력
friends = []
friends.append(input("친구이름을 입력하세요:"))
friends.append(input("친구이름을 입력하세요:"))
friends.append(input("친구이름을 입력하세요:"))
friends.append(input("친구이름을 입력하세요:"))
friends.append(input("친구이름을 입력하세요:"))
print(friends)
