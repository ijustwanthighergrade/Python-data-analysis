# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:56:04 2023

@author: Hao
"""

import pandas as pd
import matplotlib.pyplot as plt

birthrate1 = 'birthrate1.xlsx'

df = pd.read_excel(birthrate1)

# Sort the DataFrame by 'Year'
df.sort_values('Year', inplace=True)

# Set the 'Year' column as the index
df.set_index('Year', inplace=True)

# Increase the size of the plot
fig, ax = plt.subplots(figsize=(10, 4))

# Plot the grouped bar chart with thicker bars
df[['Total', 'Male', 'Female']].plot.bar(rot=0, ax=ax, width=0.8)

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Births')
ax.set_title('Total number of births (89 ~ 110 Taiwan years)')

# Show the plot
plt.show()





'''
import pandas as pd
import matplotlib.pyplot as plt

birthrate1 = 'birthrate1.xlsx'

df = pd.read_excel(birthrate1)

values = df[['Year', 'Total', 'Male', 'Female']]
print(values)

# Increase the size of the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart
values.plot.bar(x='Year', y='Female', rot=0, ax=ax)

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Births')
ax.set_title('Total Births Over the Years')

# Show the plot
plt.show()
######################################################################


import pandas as pd
import matplotlib.pyplot as plt

birthrate1 = 'birthrate1.xlsx'


df = pd.read_excel(birthrate1)

values = df[['Year','Total','Male','Female']]
print(values)

ax = values.plot.bar(x='Year', y='Total',rot=0)
plt.show()

'''