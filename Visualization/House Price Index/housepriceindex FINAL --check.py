# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:55:00 2023

@author: Hao
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

housepriceindex = 'housepriceindex1.xlsx'

script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
housepriceindex = os.path.join(script_dir, 'housepriceindex1.xlsx')
df = pd.read_excel(housepriceindex)

# Variables: Taipei City, New Taipei City, Taoyuan City, Hsinchu County and City, Taichung City, Tainan City, Kaohsiung City
cities = ['Taipei City', 'New Taipei City', 'Taoyuan City', 'Hsinchu County and City', 'Taichung City', 'Tainan City', 'Kaohsiung City']

# Reverse the order of the data
df = df[::-1]

# Create a line chart for education levels
fig, ax = plt.subplots(figsize=(13, 8))

# Set the positions for the lines
line_positions = range(len(df))

# Plot lines for each city with different colors
for city in cities:
    plt.plot(line_positions, df[city], marker='o', label=city, alpha=0.7)

# Set labels and title
plt.xlabel('Years')
plt.ylabel('House Price Index')
plt.title('House Price Index in Different Cities in Taiwan (years 89-110)')
print(df.columns)

# Set x-axis ticks and labels
plt.xticks(line_positions, df['Annual season'])

# Show legend
plt.legend()

# Show the plot
plt.show()

