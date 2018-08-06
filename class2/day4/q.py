data = [10,70,90,50,40]
data1 = [(40,50),(70,30),(20,60)] #(국어, 영어)
data2 = [{'kor':40,'eng':50},{'kor':70,'eng':30},{'kor':20,'eng':60}]

def vfn(n):
    return n
def tkfn(n):
    return n[0]
def tefn(n):
    return n[1]
def dkfn(n):
    return n['kor']

def mymax(dt,key):
    mx = None
    for n in dt:
        if mx == None or key(n) > key(mx): #open - closed 함수
            mx = n
    return mx
# open - closed기법으로 작성된 함수로 변동되는 부분은 별도의 함수로 작성해준다.
m = mymax(data2, dkfn)
print(m,m['kor'])

# m = mymax(data1, tkfn)
# print(m,m[1])

# m = mymax(data1, tkfn)
# print(m,m[0])

# m = mymax(data, vfn)
# print(m)
