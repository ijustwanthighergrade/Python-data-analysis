# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:31:22 2023

@author: Hao
"""

#####################################
##### TOTAL NUMBER OF MARRIAGES ################################################
#####################################

import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file
totalmarriages = 'number of marriages1.xlsx'
df = pd.read_excel(totalmarriages)

# Filter data for 'Male' and 'Female'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a grouped bar chart
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.35

# Set the positions for the bars
bar_positions_male = range(len(male_data))
bar_positions_female = [pos + bar_width for pos in bar_positions_male]

# Plot 'Male' and 'Female' bars
plt.bar(bar_positions_male, male_data['Total'], width=bar_width, label='Male', color='blue')
plt.bar(bar_positions_female, female_data['Total'], width=bar_width, label='Female', color='pink')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Total Number of Marriages')
plt.title('Total Number of Marriages (Male vs Female)')

# Set x-axis ticks and labels
plt.xticks([pos + bar_width/2 for pos in bar_positions_male], male_data['Year'])

# Show legend
plt.legend()

# Show the plot
plt.show()

#####################################
##### TOTAL NUMBER OF MARRIAGES PIE CHART ################################################
#####################################

import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('number of marriages1.xlsx')

# Extract relevant data for 'First Marriage' and 'Remarriage'
First_marriage = file['First Marriage'].sum()
Remarriage = file['Remarriage'].sum()


plt.figure(figsize=(10, 8))  # Set the figure size

plt.pie(
    [First_marriage, Remarriage],
    labels=['First Marriage', 'Remarriage'],
    autopct='%1.1f%%',
)

plt.title('Total Number of Marriages years 89 - 110')
plt.show()


##########################################
##### TOTAL NUMBER OF Male MARRIAGES ###########################################
##########################################

import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('number of marriages1.xlsx')

# Filter data for 'Male'
Male_data = file[file['Sex'] == 'Male']

# Extract relevant data for 'First Marriage' and 'Remarriage'
First_marriage = Male_data['First Marriage'].sum()
Remarriage = Male_data['Remarriage'].sum()

plt.figure(figsize=(10, 8))  # Set the figure size

colors = ['lightblue', 'skyblue']

plt.pie(
    [First_marriage, Remarriage],
    labels=['First Marriage', 'Remarriage'],
    autopct='%1.1f%%',
    colors=colors
)

plt.title('Total Number of Marriages (Male) years 89 - 110')
plt.show()



############################################
##### TOTAL NUMBER OF Female MARRIAGES #########################################
############################################

import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('number of marriages1.xlsx')

# Filter data for 'Female'
female_data = file[file['Sex'] == 'Female']

# Extract relevant data for 'First Marriage' and 'Remarriage'
First_marriage = female_data['First Marriage'].sum()
Remarriage = female_data['Remarriage'].sum()

plt.figure(figsize=(10, 8))  # Set the figure size

colors = ['pink', 'violet']

plt.pie(
    [First_marriage, Remarriage],
    labels=['First Marriage', 'Remarriage'],
    autopct='%1.1f%%',
    colors=colors
)

plt.title('Total Number of Marriages (Female) years 89 - 110')
plt.show()











