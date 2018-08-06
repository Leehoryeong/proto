def fn():
    my = [10,20,30]
    print(my)
    print(id(my))
    return my #리턴하게되면 함수가 끝난다 return의 역할은 my주소값을 rst로 보내주는것 (reference count가 0이 되는걸 막음)
# fn()
#fn함수가 실행되면 heap메모리에 리스트가 생성되고 지역변수인 my가 그 주소를 참조한다
#함수의 사용이 끝난 이후에는 my가 증발하게 되는데 참조변수가 0 이되면 heap메모리의 데이터 주소도 함께 증발한다.

# rst = fn()
# print(id(rst))
# print('rst:', rst)


def yaksu(num):
    y = [n for n in range(1, num+1) if num%n == 0]
    return y
rst = yaksu(10)
print(rst)
