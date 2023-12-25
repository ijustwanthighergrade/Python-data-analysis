# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:01:54 2023

@author: Hao
"""

import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('age1.xlsx')

# Assuming columns D to O contain the values you want for the pie chart
# Adjust the column selection as needed
total_under_15 = file['Under 15 years old'].sum()
total_15_19 = file['15-19 years old'].sum()
total_20_24 = file['20-24 years old'].sum()
total_25_29 = file['25-29 years old'].sum()
total_30_34 = file['30-34 years old'].sum()
total_35_39 = file['35-39 years old'].sum()
total_40_44 = file['40-44 years old'].sum()
total_45_49 = file['45-49 years old'].sum()
total_50_54 = file['50-54 years old'].sum()
total_55_59 = file['55-59 years old'].sum()
total_60_64 = file['60-64 years old'].sum()
total_over_65 = file['Over 65 years old'].sum()

# Calculate explode values to increase the distance between slices
explode = (0.4, 0.7, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.7, 0.7, 0.7, 0.7)

plt.figure(figsize=(10, 8))  # Set the figure size

plt.pie(
    [total_under_15, total_15_19, total_20_24, total_25_29, total_30_34, total_35_39, total_40_44, total_45_49, total_50_54, total_55_59, total_60_64, total_over_65],
    labels=['Under 15 years old', '15-19 years old', '20-24 years old', '25-29 years old', '30-34 years old', '35-39 years old', '40-44 years old', '45-49 years old', '50-54 years old', '55-59 years old', '60-64 years old', 'Over 65 years old'],
    autopct='%1.1f%%',
    explode=explode  # Increase the distance between slices
)

plt.title('Total Average Number of Marriages divided by age from years 89 - 110')
plt.show()


