# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:18:38 2023

@author: Hao
"""
##### Midterm population (person) #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Population (person)' is the new population column name
population_column = 'Population (person)'

# Create a line plot for Population with purple color
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[population_column], label='Population (person)', marker='o', color='blue')  # Plot Population

# Set x-axis ticks using the actual values from 'Population (person)' column
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Population over the years Taiwan years 89-110')
plt.xlabel('Statistical Period')
plt.ylabel('Population (person) in millions')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()







##### Average exchange rate #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Average exchange rate (yuan/USD)' is the new average exchange rate column name
average_exchange_rate_column = 'Average exchange rate (yuan/USD)'

# Create a line plot for Average exchange rate with purple color
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[average_exchange_rate_column], label='Average exchange rate (yuan/USD)', marker='o', color='purple')  # Plot Average exchange rate

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Average Exchange Rate over the years Taiwan years 80-110')
plt.xlabel('Statistical Period')
plt.ylabel('Exchange Rate (yuan/USD)')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()



##### Economic growth rate (%) #######################################################


import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Economic growth rate (%)' is the new economic growth rate column name
economic_growth_rate_column = 'Economic growth rate (%)'

# Create a line plot for Economic growth rate
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[economic_growth_rate_column], label='Economic growth rate (%)', marker='o', color='gold')  # Plot Economic growth rate

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Economic Growth Rate over the years Taiwan years 80-110')
plt.xlabel('Statistical Period')
plt.ylabel('Growth Rate (%)')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

##### GDP #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Gross domestic product GDP (nominal value, million yuan)' is the GDP column name
gdp_column = 'Gross domestic product GDP (nominal value, million yuan)'

# Create a line plot for GDP only
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[gdp_column], label='Gross domestic product GDP (nominal value, million yuan)', marker='o', color='brown')  # Plot GDP

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Income over the years Taiwan years 80-110 (Gross Domestic Product GDP)')
plt.xlabel('Statistical Period')
plt.ylabel('Amount in Millions yuan')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


##### Average GDP per capita #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Average GDP per capita (nominal value, yuan)' is the new GDP column name
gdp_column = 'Average GDP per capita (nominal value, yuan)'

# Create a line plot for Average GDP per capita
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[gdp_column], label='Average GDP per capita (nominal value, yuan)', marker='o', color='red')  # Plot Average GDP per capita

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Income over the years Taiwan years 80-110 (Average GDP per capita)')
plt.xlabel('Statistical Period')
plt.ylabel('Amount in Yuan')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


##### GNI #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Gross national income GNI (nominal value, million yuan)' is the new GNI column name
gni_column = 'Gross national income GNI (nominal value, million yuan)'

# Create a line plot for Gross national income GNI
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[gni_column], label='Gross national income GNI (nominal value, million yuan)', marker='o', color='skyblue')  # Plot GNI

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Income over the years Taiwan years 80-110 (Gross National Income GNI)')
plt.xlabel('Statistical Period')
plt.ylabel('Amount in Millions yuan')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


##### Average GNI per capita #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Average GNI per person (nominal value, yuan)' is the new GNI per person column name
gni_per_person_column = 'Average GNI per person (nominal value, yuan)'

# Create a line plot for Average GNI per person
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[gni_per_person_column], label='Average GNI per person (nominal value, yuan)', marker='o', color='green')  # Plot Average GNI per person

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Income over the years Taiwan years 80-110 (Average GNI per person)')
plt.xlabel('Statistical Period')
plt.ylabel('Amount in Yuan')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


##### National income #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'National income (nominal value, million yuan)' is the new national income column name
national_income_column = 'National income (nominal value, million yuan)'

# Reverse the order of the data for the line plot
reversed_data = df[national_income_column][::-1]

# Create a line plot for National income
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(reversed_data, label='National income (nominal value, million yuan)', marker='o', color='grey')  # Plot National income

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Income over the years Taiwan years 80-110 (National Income)')
plt.xlabel('Statistical Period')
plt.ylabel('Amount in Millions yuan')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


##### Average income per person #######################################################

import pandas as pd
import matplotlib.pyplot as plt

# File path to the Excel file
file_path = 'income1.xlsx'

# Load the data into a pandas DataFrame
df = pd.read_excel(file_path)

# Assuming 'Average income per person (nominal value, yuan)' is the new average income per person column name
average_income_per_person_column = 'Average income per person (nominal value, yuan)'

# Create a line plot for Average income per person
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df[average_income_per_person_column], label='Average income per person (nominal value, yuan)', marker='o', color='slateblue')  # Plot Average income per person

# Set x-axis ticks using the 'Statistical Period' column values
tick_positions = range(len(df))
tick_labels = df['Statistical Period']

plt.xticks(tick_positions, tick_labels, rotation=45, ha='right')

plt.title('Income over the years Taiwan years 80-110 (Average Income per person)')
plt.xlabel('Statistical Period')
plt.ylabel('Amount in Yuan')
plt.legend()  # Display legend
plt.grid(True)  # Display grid
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


