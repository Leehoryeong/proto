data = [('홍길동',20),('이순신',30)]
for n, a in data:
    # print("이름%s 나이:%s"%(n,a))
    print("이름:{0} 나이:{1}".format(n,a))

for d in data:
    # print("이름%s 나이:%s"%(n,a))
    print("이름:{0} 나이:{1}".format(*d))
