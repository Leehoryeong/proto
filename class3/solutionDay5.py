from statistics import mean

import csv
#형변환, 튜플로 저장
data=[]
crime_file=open('02. crime_in_Seoul.csv','r')
rdr_crime=csv.reader(crime_file)
next(rdr_crime)
for line in rdr_crime:
    line = [ n.replace(',','') for n in line]
    data.append( (line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]),int(line[6]),int(line[7]),int(line[8]),int(line[9]),int(line[10])))

#살인범죄 발생 top5
def Murder_Occur():
    s= sorted(data, key=lambda n:n[1], reverse=True)
    #print(s)
    print("살인 발생 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"발생건수",s[i-1][1])

#살인범죄 검거 top5
def Murder_Arrest():
    s= sorted(data, key=lambda n:n[2], reverse=True)
    #print(s)
    print("살인 검거 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"검거건수",s[i-1][2])

#강도범죄 발생 top5
def burglar_Occur():
    s= sorted(data, key=lambda n:n[3] ,reverse=True)
    print("강도 발생 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"발생건수",s[i-1][3])

#강도범죄 검거  top5
def burglar_Arrest():
    s= sorted(data, key=lambda n:n[4] ,reverse=True)
    print("강도 검거 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"검거건수",s[i-1][4])

#강간범죄  발생  top5
def rape_Occur() :
    s= sorted(data, key=lambda n:n[5] ,reverse=True)
    print("강간 발생 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"발생건수",s[i-1][5])

#강간범죄  검거 top5
def rape_Arrest():
    s= sorted(data, key=lambda n:n[6] ,reverse=True)
    print("강간 검거 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"검거건수",s[i-1][6])

#절도범죄 발생 top5
def theft_Occur():
    s= sorted(data, key=lambda n:n[7] ,reverse=True)
    print("절도 발생 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"발생건수",s[i-1][7])

# 절도범죄 검거 top5
def theft_Arrest():
    s= sorted(data, key=lambda n:n[8] ,reverse=True)
    print("절도 검거 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"검거건수",s[i-1][8])

# 폭력범죄 발생 top5
def violence_Occur():
    s= sorted(data, key=lambda n:n[9] ,reverse=True)
    print("폭력 발생 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"발생건수",s[i-1][9])

# 폭력범죄 검거 top5
def violence_Arrest():
    s= sorted(data, key=lambda n:n[10] ,reverse=True)
    print("폭력 검거 top 5")
    print('='*60)
    for i in range(1,6):
        print("top",i,"->",s[i-1][0],"검거건수",s[i-1][10])

#main
crime_list={1:'살인',2:'강도',3:'강간',4:'절도',5:'폭력'}
OorA={1:'발생',2:'검거'}
menu = ['살인', '강도', '강간', '절도', '폭력']
YorN='y'

#초기화면
print("서울 지역 범죄 현황에 대해 알아봅시다")
print()
for m in range(1,11,2):
    print('%s 범죄 평균 건수는 %.1f 입니다.'% (menu[m//2] ,mean( [n[m] for n in data])))
print('='*60)
while YorN=='y':
    print(crime_list)
    ch1=int(input("자세한 범죄 유형을 선택하세요 : "))

    print(OorA)
    ch2=int(input("발생과 검거를 선택하세요 : "))

    if(ch1 in range(1,6)and(ch2 in range(1,3))):
        if(ch1==1 and ch2==1):
            Murder_Occur() #살인 발생
            print()
        elif(ch1==1 and ch2==2):
            Murder_Arrest() #살인 검거
            print()
        elif(ch1==2 and ch2==1):
            burglar_Occur() #강도 발생
            print()
        elif(ch1==2 and ch2==2):
            burglar_Arrest()#강도 검거
            print()
        elif(ch1==3 and ch2==1):
            rape_Occur() #강간 발생
            print()
        elif(ch1==3 and ch2==2):
            rape_Arrest()#강간 검거
            print()
        elif(ch1==4 and ch2==1):
            theft_Occur()#절도 발생
            print()
        elif(ch1==4 and ch2==2):
            theft_Arrest()#절도 검거
            print()
        elif(ch1==5 and ch2==1):
            violence_Occur() #폭력 발생
            print()
        elif(ch1==5 and ch2==2):
            violence_Arrest()#폭력 검거
            print()
    else:
        print()
        print("숫자를 잘못 입력하셨습니다.")

    YorN=input("계속: y, 그만: n 를 입력하세요 : ")
