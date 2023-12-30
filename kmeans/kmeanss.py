# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 13:37:46 2023

@author: j9103
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

import os
from matplotlib import rcParams

# 設定字型，使用支援中文的字型（例如 Microsoft JhengHei）
rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# 顯示全形字符警告
rcParams['axes.unicode_minus'] = False
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, '房價與結婚意願之相關分析_1214修改版 的副本 (回覆) (1).xlsx')

# Reading the Excel file with an explicit encoding
df = pd.read_excel(file_path)

# Mapping age ranges to numeric values
age_mapping = {'21～29': 25, '30～39': 35, '40～49': 45, '50～59': 55, '60以上': 65}
df['年齡數值'] = df['您的年齡'].map(age_mapping)

# Mapping salary ranges to numeric values
salary_mapping = {'0～19999': 10000, '20000～39999': 30000, '40000～59999': 50000, '60000～79999': 70000, '80000以上': 90000}
df['月薪資數值'] = df['目前月薪資水平(台幣)'].map(salary_mapping)

# Selecting relevant features for K-means clustering
features = ['年齡數值', '月薪資數值', '請問買房影響您結婚意願的程度為？']
data_for_clustering = df[features].dropna()

# Applying K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(data_for_clustering)

# Adding cluster information to the dataframe
data_for_clustering['Cluster'] = clusters

# Creating a correlation matrix and visualizing it using a heatmap
correlation_matrix = data_for_clustering.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap of Correlation Between Age, Monthly Salary, and Influence on Marriage Intention')
plt.show()

"""
Heatmap with clearly labeled x- and y-axes. This figure shows the correlation between "age", "monthly salary level" and "the extent to which buying a house affects the intention to get married". Correlation coefficients are represented in different colors
, helps us intuitively see the correlation strength between different features.
"""