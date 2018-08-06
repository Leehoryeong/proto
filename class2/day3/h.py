#파이썬의 모든 변수는 참조변수(포인트변수)

myList = [10,20,30] # List( [10,20,30] )
# 전역변수myList는static에 생성되고 리스트값은
# heap 메모리에 리스트 객체가 생성되는데 myList는 heap메모리 쪽의 주소를 참조한다.
# my = myList #shallow copy : heap메모리의 주소를 가져온다(주소만 복사)
# my = [10,20,30] #같은 값이어도 주소가 달라진다

my = myList.copy() #deep copy : (동일한 리스트객체 복사본을 별도 힙영역에)
#카피본과 같은 것을 별도의 주소를 만들어 복사 (heap 메모리에 새로운 주소 생성)

print(id(myList)) #실제로 참조하고 있는 주소 => heap메모리에 가서 myList가 참조하는 주소를 가져온다.

print(id(my)) #reference count 2 => 같은 주소를 참조하는 변수는 2개

print(myList) #my와 myList가 같은 주소를 참조하고 있어서 하나를 변경하면 두개 모두 바뀐다.
print(my)
