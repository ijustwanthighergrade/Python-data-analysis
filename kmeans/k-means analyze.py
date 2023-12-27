# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 06:26:35 2023

@author: j9103
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_path)
    return pd.read_excel(file_path)

def preprocess_data(data):
   
    age_mapping = {'21～29': 25, '30～39': 35, '40～49': 45, '50～59': 55, '60以上': 65}
    salary_mapping = {'0～19999': 10000, '20000～39999': 30000, '40000～59999': 50000, '60000～79999': 70000, '80000以上': 90000}
    marital_status_mapping = {'否': 0, '是': 1}

    data['Age_Num'] = data['您的年齡'].map(age_mapping)
    data['Salary_Num'] = data['目前月薪資水平(台幣)'].map(salary_mapping)
    data['Marital_Status_Num'] = data['您是否已婚？'].map(marital_status_mapping)

    return data[['Age_Num', 'Salary_Num', 'Marital_Status_Num']].dropna()

def perform_clustering(data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    data['Cluster'] = kmeans.labels_
    return data

file_path = '房價與結婚意願之相關分析_1214修改版 的副本 (回覆).xlsx'
data = load_data(file_path)
preprocessed_data = preprocess_data(data)

clustered_data = perform_clustering(preprocessed_data)

# 散點圖
# 1. 年齡與月薪
plt.figure(figsize=(12, 6))
sns.scatterplot(data=clustered_data, x='Age_Num', y='Salary_Num', hue='Cluster', palette='viridis')
plt.title('年齡與月薪的散點圖（KMeans 聚類）')
plt.xlabel('年齡')
plt.ylabel('月薪 (新台幣)')
plt.show()

# 2. 婚姻狀態與月薪
plt.figure(figsize=(12, 6))
sns.scatterplot(data=clustered_data, x='Marital_Status_Num', y='Salary_Num', hue='Cluster', palette='viridis', style='Marital_Status_Num')
plt.title('婚姻狀態與月薪的散點圖（KMeans 聚類）')
plt.xlabel('婚姻狀態（0: 未婚, 1: 已婚）')
plt.ylabel('月薪 (新台幣)')
plt.show()

# 3. 年齡、月薪與婚姻狀態
plt.figure(figsize=(12, 6))
sns.scatterplot(data=clustered_data, x='Age_Num', y='Salary_Num', hue='Cluster', palette='viridis', style='Marital_Status_Num')
plt.title('年齡、月薪與婚姻狀態的綜合散點圖（KMeans 聚類）')
plt.xlabel('年齡')
plt.ylabel('月薪 (新台幣)')
plt.show()
