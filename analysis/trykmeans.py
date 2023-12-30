import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import sys
import os
import django
import seaborn as sns

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analysis.settings")
django.setup()
# 假設 df 為包含你的資料的 DataFrame，其中每一列是一位受訪者，每一欄是一個特徵
# 這邊使用部分資料作為範例
from home.models import MarriageSurvey
# survey_data = MarriageSurvey.objects.values('gender', 'education', 'age', 'salary', 'is_married', 'marriage_intention')
# data =pd.DataFrame(list(survey_data))
# alliwanttoshow={}
# alliwanttoshow['gender']=['男','女']
# alliwanttoshow['education_levels'] = ['小學','國中','高中','大學','碩士','博士']
# alliwanttoshow['age'] = [
# '17歲(含)以下',
# '18～20',
# '21～29',
# '30～39',
# '40～49',
# '50～59',
# '60～69',
# '70～79',
# '80～89',
# '90以上']
# alliwanttoshow['income'] = [
# '0～19999',
# '20000～39999',
# '40000～59999',
# '60000~79999',
# '80000~99999',
# '100000~119000',
# '120000～139999',
# '140000以上',
# '家管',
# '學生無收入'
# ]
# alliwanttoshow['is_married']=["是","否"]
# # 將類別型資料轉換為數值

# # Mapping age ranges to numeric values
# age_mapping = {
#     '17歲(含)以下': 17, '18～20': 19, '21～29': 25, '30～39': 35, '40～49': 45,
#     '50～59': 55, '60～69': 65, '70～79': 75, '80～89': 85, '90以上': 95
# }
# data['age'] = data['age'].map(age_mapping)

# # Mapping salary ranges to numeric values
# salary_mapping = {
#     '0～19999': 10000, '20000～39999': 30000, '40000～59999': 50000,
#     '60000~79999': 70000, '80000~99999': 90000, '100000~119000': 110000,
#     '120000～139999': 130000, '140000以上': 145000, '家管': 0, '學生無收入': 0
# }
# data['salary'] = data['salary'].map(salary_mapping)

# data['is_married'] = data['is_married'].apply(lambda x: 1 if x == '是' else 0)
# data = pd.get_dummies(data, columns=['gender', 'education'])

# # 處理缺失值
# data = data.dropna()

# # 將資料進行標準化
# scaler = StandardScaler()
# data_scaled = scaler.fit_transform(data)

# # 使用 K 均值聚類
# kmeans = KMeans(n_clusters=3, random_state=42)
# data['cluster'] = kmeans.fit_predict(data_scaled)

# # 進行主成分分析 (PCA) 以便視覺化
# pca = PCA(n_components=2)
# data_pca = pca.fit_transform(data_scaled)
# data['pca1'] = data_pca[:, 0]
# data['pca2'] = data_pca[:, 1]

# # 視覺化集群
# plt.scatter(data['pca1'], data['pca2'], c=data['cluster'], cmap='viridis')
# plt.title('K-Means Clustering')
# plt.show()


# 假設你的資料框為 df
survey_data = MarriageSurvey.objects.values('gender', 'education', 'age')
df = pd.DataFrame(list(survey_data))
df['gender'] = df['gender'].map({'男': 0, '女': 1})
education_mapping = {'小學': 0, '國中': 1, '高中': 2, '大學': 3, '碩士': 4, '博士': 5}
df['education'] = df['education'].map(education_mapping)
# Mapping age ranges to numeric values
age_mapping = {
    '17歲(含)以下': 17, '18～20': 19, '21～29': 25, '30～39': 35, '40～49': 45,
    '50～59': 55, '60～69': 65, '70～79': 75, '80～89': 85, '90以上': 95
}
df['age'] = df['age'].map(age_mapping)

# 特徵選取
features = df[['gender', 'education', 'age']]

# 資料標準化
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# K 均值聚類
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(features_scaled)

# 可以印出每個群組的資料
print(df)

# 設定 seaborn 風格
sns.set(style="whitegrid")

# 使用散點圖，hue 參數表示色彩對應的特徵
sns.scatterplot(data=df, x='education', y='age', hue='Cluster', palette='viridis')

# 設定標籤
plt.xlabel('Education Level')
plt.ylabel('Age')

# 顯示圖例
plt.legend(title='Cluster')

# 顯示圖表
plt.show()