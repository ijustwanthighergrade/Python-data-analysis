# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:19:36 2023

@author: Hao
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Define the file containing house price index data
housepriceindex = 'housepriceindex1.xlsx'

# Read the data into a Pandas DataFrame
df_house_price = pd.read_excel(housepriceindex)

# Define a list of cities for which the analysis will be conducted
cities = ['Taipei City', 'New Taipei City', 'Taoyuan City', 'Hsinchu County and City', 'Taichung City', 'Tainan City', 'Kaohsiung City']

# Reverse the order of the data in the DataFrame
df_house_price = df_house_price[::-1]

# Create a new figure and axis for the plot
fig, ax = plt.subplots(figsize=(13, 8))

# Set the positions for the lines on the x-axis
line_positions = range(len(df_house_price))

# Plot lines for each city with different colors
for city in cities:
    plt.plot(line_positions, df_house_price[city], marker='o', label=city, alpha=0.7)
    
# Set labels and title for the plot
plt.xlabel('Years')
plt.ylabel('House Price Index')
plt.title('House Price Index in Different Cities in Taiwan (years 89-110)')

# Set x-axis ticks and labels with custom locator
ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
plt.xticks(line_positions[::len(line_positions)//10], df_house_price['Years'][::len(df_house_price)//10])

# Show legend for the plotted lines
plt.legend()

# Display the plot
plt.show()


