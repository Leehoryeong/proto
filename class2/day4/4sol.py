from statistics import mean,stdev
data=[]
def makeData():
    fp = open("births.txt", 'r')
    for rd in fp:
        y,m,f = rd.split(',')
        data.append( (y, int(m), int(f) ) )
    fp.close()

def showAll():
    for y,m,f in data:
        print("년도:",y)
        print("남아:",m)
        print("여아:",f)
        print("="*20)

def totM():
    print("남아총합:", sum( [n[1] for n in data]  ))
def maxM():
    mx = max( data, key=lambda n:n[1] )
    print( '남아출생수가 가장 많은년도', mx[0], '출생수', mx[1] )
def meanF():
    print( '평균 여아 출생수:%.2f'% mean( [n[2] for n in data]  ) )
def top5F():
    # 여아출생수가 가장 많은 top5 년도와 출생수
    topF = sorted(data, key=lambda n:n[2] ,reverse=True)[:5]
    for y,m,f in topF:
        print('년도:', y, "여아출생수:", f)
def stddevM():
    print("남아표준편차:", stdev( [n[1] for n in data]  ))

def wrongSel():
    print('1~7번까지 선택하세요')
def main():
    makeData()
    while True:
        print( '미국 출생아 통계')
        print('='*20)
        print( '1. 전체출력.','2. 남아수총합','3. 남아출생수가 가장 많은년도와 출생수',
               '4. 평균 여아 출생수','5. 여아출생수가 가장 많은 top5 년도와 출생수',
               '6. 남아출생의 표준편차','7.종료', sep='\n')
        menu = {1:showAll,2:totM,3:maxM,4:meanF,5:top5F,6:stddevM,7:exit}
        selMenu = int( input('메뉴를 선택하세요:') )
        menu.get( selMenu, wrongSel  )()
        # menu[selMenu]()
if __name__ == '__main__':
    main()




# makeData()
# stddevM()
# top5F()
# meanF()
# totM()
# showAll()







# fp = open("births.txt", 'r')
# for rd in fp:
#     y,m,f = rd.split(',')
#     data.append( (y,int(m),int(f) ) )
#     print("년도:",y)
#     print("남아:",m)
#     print("여아:",f)
#     print("="*20)
# fp.close()
