import csv,sys,os
import django
data = csv.reader(open("C:/Users/DAIYUNWU/Desktop/Python-data-analysis/analysis/房價與結婚意願之相關分析_1214修改版 的副本 (回覆) - 表單回應 1.csv"),delimiter=",")
data=next(data)
for row in data:
	print(row)
