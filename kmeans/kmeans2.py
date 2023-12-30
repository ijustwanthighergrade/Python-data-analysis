# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:47:04 2023

@author: j9103
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Load the data

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, '房價與結婚意願之相關分析_1214修改版 的副本 (回覆) (1).xlsx')

data = pd.read_excel(file_path)

# Map age and income to numerical values
age_mapping = {'21～29': 25, '30～39': 35, '40～49': 45, '50～59': 55, '60以上': 65}
salary_midpoints = {
    '0～19999': 10000, 
    '20000～39999': 30000, 
    '40000～59999': 50000, 
    '60000～79999': 70000, 
    '80000以上': 90000
}
data['年齡數值'] = data['您的年齡'].map(age_mapping)
data['月薪資水平(台幣)_中點'] = data['目前月薪資水平(台幣)'].map(salary_midpoints)

# Select relevant features for clustering
features = data[['年齡數值', '月薪資水平(台幣)_中點', '您目前是否有結婚意願(不論單身與否)\n已婚者可以是否後悔結婚來考量']]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=0)  # Adjust the number of clusters as needed
clusters = kmeans.fit_predict(features_scaled)

# Add cluster information to the dataframe
data['Cluster'] = clusters

print(data.groupby('Cluster').mean())
"""
Visualization
Cluster Centers and Mean Values:

The script prints the mean values of each feature 
(age, monthly income, and marriage intention score) for each cluster. 
This helps in understanding the average characteristics of each cluster. 
For example, one cluster might have a younger average age and lower income, 
while another might have an older average age and higher income.
Visualization:

A scatter plot showing the distribution of your data points across the defined clusters. 
Each point represents an individual in your dataset, plotted based on their age and monthly income. The color of the points indicates the cluster they belong to. This visualization helps in seeing how the data points are grouped and whether any patterns or distinct clusters emerge based on the chosen features.
"""
plt.figure(figsize=(12, 8))
sns.scatterplot(x='年齡數值', y='月薪資水平(台幣)_中點', hue='Cluster', data=data)
plt.title('K-Means Clustering of Age, Monthly Income, and Marriage Intention')
plt.xlabel('Age')
plt.ylabel('Monthly Income')
plt.show()
