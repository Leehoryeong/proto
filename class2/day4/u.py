# import statistics
from statistics import mean, median, stdev

data = [10,70,90,50,40]
data1 = [(40,50),(70,30),(20,60)] #(국어, 영어)
data2 = [{'kor':40,'eng':50},{'kor':70,'eng':30},{'kor':20,'eng':60}]

rst =mean(data)
print(rst)
rst =median(data)
print(rst)
rst = stdev(data)
print(rst)
