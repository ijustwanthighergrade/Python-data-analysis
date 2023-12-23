import pandas as pd
from apyori import apriori
import os

# 读取数据
script_dir = os.path.dirname(os.path.abspath(__file__))
age = os.path.join(script_dir, "collect.xlsx")

# 指定要读取的非连续行的索引（行索引从0开始）
selected_columns = [1, 2, 3, 4, 5, 6]

# 读取特定列的数据
df = pd.read_excel(age, usecols=selected_columns)


df = df.astype(str)  # Use this line for replacement

# 将数据转换为列表
data_list = df.values.tolist()
# 输出数据列表
# print(data_list)

# 使用apriori算法
results = list(apriori(data_list, min_support=0.1, min_confidence=0.1, min_lift=1.5, max_length=2))

# print(results)
# 
for result in results:
    pair = result[0] 
    ##print(pair) ## ex. frozenset({'Basketball', 'Socks'})
    products = [x for x in pair]
    print(products) # ex. ['Basketball', 'Socks']
    print("Rule: " + products[0] + " →" + products[1])
    print("Support: " + str(result[1]))
    print("Confidence: " + str(result[2][0][2]))
    print("Lift: " + str(result[2][1][3]))
    print("==================================")
