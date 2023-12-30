# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:06:59 2023

@author: j9103
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, '房價與結婚意願之相關分析_1214修改版 的副本 (回覆) (1).xlsx')

data = pd.read_excel(file_path)

data.head()

age_mapping = {'21～29': 25, '30～39': 35, '40～49': 45, '50～59': 55, '60以上': 65}
data['年齡數值'] = data['您的年齡'].map(age_mapping)


age_marriage_intention = data.groupby('年齡數值')['您目前是否有結婚意願(不論單身與否)\n已婚者可以是否後悔結婚來考量'].mean()
"""
繪製折線圖
顯示不同年齡組別的平均結婚意願，有助於理解不同年齡層對結婚的看法和意願如何隨年齡變化。
"""
plt.figure(figsize=(10, 6))
plt.plot(age_marriage_intention, marker='o', linestyle='-', color='b')
plt.title('Average Marriage Intention by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Marriage Intention Score')
plt.xticks(ticks=age_marriage_intention.index)
plt.grid(True)
plt.show()



# 數據預處理
salary_midpoints = {
    '0～19999': 10000, 
    '20000～39999': 30000, 
    '40000～59999': 50000, 
    '60000～79999': 70000, 
    '80000以上': 90000
}
data['月薪資水平(台幣)_中點'] = data['目前月薪資水平(台幣)'].map(salary_midpoints)
"""
創建傘點圖箱形的中間線：
表示中位數，即該收入範圍內一半人的結婚意願得分高於此值，另一半低於此值。
箱形的上下界：表示第一四分位數和第三四分位數，也就是該收入範圍內25%和75%的人的結婚意願得分分佈範圍。
突出的點：可能表示異常值，即特別高或特別低的結婚意願得分。
"""
plt.figure(figsize=(12, 8))
sns.boxplot(x='月薪資水平(台幣)_中點', y='您目前是否有結婚意願(不論單身與否)\n已婚者可以是否後悔結婚來考量', data=data)
plt.title('Relationship Between Monthly Income and Marriage Intention')
plt.xlabel('Monthly Income (NTD)')
plt.ylabel('Marriage Intention Score')
plt.grid(True)
plt.show()

