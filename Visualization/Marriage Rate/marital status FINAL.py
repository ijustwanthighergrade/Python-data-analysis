# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:54:10 2023

@author: Hao
"""
#####################################
##### MARITAL STATUS MALES ################################################
#####################################
import pandas as pd
import matplotlib.pyplot as plt

maritalstatus = 'maritalstatus1.xlsx'

df = pd.read_excel(maritalstatus)

# Filter data for 'Male'
male_data = df[df['Sex'] == 'Male']

# Reverse the order of the data
male_data = male_data[::-1]

# Create a grouped bar chart for 'Male' Unmarried, Divorced, and Widowed values
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.25

# Set the positions for the bars
bar_positions_male_unmarried = range(len(male_data))

bar_positions_male_divorced = [pos + bar_width for pos in bar_positions_male_unmarried]
bar_positions_male_widowed = [pos + 2 * bar_width for pos in bar_positions_male_unmarried]

# Plot 'Male' bars for 'Unmarried', 'Divorced', and 'Widowed'
plt.bar(bar_positions_male_unmarried, male_data['Unmarried'], width=bar_width, label='Male (Unmarried)', color='blue')
plt.bar(bar_positions_male_divorced, male_data['Divorced'], width=bar_width, label='Male (Divorced)', color='lightblue')
plt.bar(bar_positions_male_widowed, male_data['Widowed'], width=bar_width, label='Male (Widowed)', color='lightskyblue')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Marital Status Distribution (Male)')

# Set x-axis ticks and labels
ticks_positions = [pos + bar_width for pos in bar_positions_male_unmarried]
plt.xticks(ticks_positions, male_data['Year'])

# Show legend
plt.legend()

# Show the plot
plt.show()



#####################################
##### MARITAL STATUS FEMALES ################################################
#####################################


import pandas as pd
import matplotlib.pyplot as plt

maritalstatus = 'maritalstatus1.xlsx'

df = pd.read_excel(maritalstatus)

# Filter data for 'Female'
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
female_data = female_data[::-1]

# Create a grouped bar chart for 'Female' Unmarried, Divorced, and Widowed values
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.25

# Set the positions for the bars
bar_positions_female_unmarried = range(len(female_data))

bar_positions_female_divorced = [pos + bar_width for pos in bar_positions_female_unmarried]
bar_positions_female_widowed = [pos + 2 * bar_width for pos in bar_positions_female_unmarried]

# Plot 'Female' bars for 'Unmarried', 'Divorced', and 'Widowed'
plt.bar(bar_positions_female_unmarried, female_data['Unmarried'], width=bar_width, label='Female (Unmarried)', color='pink')
plt.bar(bar_positions_female_divorced, female_data['Divorced'], width=bar_width, label='Female (Divorced)', color='violet')
plt.bar(bar_positions_female_widowed, female_data['Widowed'], width=bar_width, label='Female (Widowed)', color='plum')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Marital Status Distribution (Female)')

# Set x-axis ticks and labels
ticks_positions = [pos + bar_width for pos in bar_positions_female_unmarried]
plt.xticks(ticks_positions, female_data['Year'])

# Show legend
plt.legend()

# Show the plot
plt.show()




#####################################
##### MARITAL STATUS PIE CHART ################################################
#####################################

import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('maritalstatus1.xlsx')

# Filter data for 'Male' and 'Female'
male_data = file[file['Sex'] == 'Male']
female_data = file[file['Sex'] == 'Female']

# Calculate total values for 'Male' and 'Female'
total_male = male_data['Total'].sum()
total_female = female_data['Total'].sum()

plt.figure(figsize=(10, 8))  # Set the figure size

# Set colors for 'Male' and 'Female'
colors = ['lightblue', 'pink']

plt.pie(
    [total_male, total_female],
    labels=['Male', 'Female'],
    autopct='%1.1f%%',
    colors=colors  # Set colors for each slice
)

plt.title('Total of out-of-marriage males and females from years 89-110')
plt.show()


#print("Male Unique Values:", male_data['Total'].unique())
#print("Female Unique Values:", female_data['Total'].unique())
