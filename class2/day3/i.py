def fn(my):
    print(id(my))
    print(my)
    my[0] = 100
    my.append(40)
    my.append(50)

d = [10,20,30]
print(id(d))
fn(d) #my 와 d 모두 같은 주소 참조 shallow copy
print(d)
