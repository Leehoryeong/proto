fp = open("births.txt",'r')
data = []
for rd in fp:
    y,m,f = rd.split(',') #rd는 문자열
    data.append({"년도":int(y),"남아":int(m),"여아":int(f)})
    print("년도:", y)
    print("남아:", m)
    print("여아:", f)


#2번
def sumM(dt):
    birthM = (dt[n]['남아'] for n in range(0,len(dt)))
    print(sum(birthM))
sumM(data)

# 3번
def dkfn(n):
    return n['남아']
def largeM(dt,key):
    mx = None
    for n in dt:
        if mx == None or key(n)> key(mx):
            mx = n
    return mx
m = largeM(data,dkfn)
print(m['남아'])
from statistics import mean, median, stdev

#4번
def avgF(dt):
    birthF = (dt[n]["여아"] for n in range(0,len(dt)))
    return mean(birthF)

print(avgF(data))

#5번
def large5F(dt):
    best5 = sorted(dt, key = lambda n:n['여아'], reverse=True)
    girls = (best5[x]["여아"] for x in range(0,5))
    years = (best5[x]["년도"] for x in range(0,5))
    return list(girls), list(years)
for i in range(0,5):
    print('여아출생수',large5F(data)[0][i],'년도:',large5F(data)[1][i])

#6번
def stdM(dt):
    birthM = (dt[n]['남아'] for n in range(0,len(dt)))
    print(stdev(birthM))
stdM(data)
fp.close()
#
#
#
# # 1) 문자열을 읽어 아래와 같이 출력.
# # 2) 남아수 총합
# # 3) 남아출생수가 가장 많은년도와 출생수
# # 4) 평균 여아 출생수
# # 5) 여아출생수가 가장 많은 top5 년도와 출생수
# # 6) 남아출생의 표준편차
