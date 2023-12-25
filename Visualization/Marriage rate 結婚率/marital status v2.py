# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 06:05:20 2023

@author: Hao
"""

############### UNMARRIED ##########################################################

import pandas as pd
import matplotlib.pyplot as plt

maritalstatus = 'maritalstatus1.xlsx'

df = pd.read_excel(maritalstatus)

# Filter data for 'Male' and 'Female'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a bar chart for 'Male' and 'Female' Unmarried values
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.35

# Set the positions for the bars
bar_positions_male_unmarried = range(len(male_data))
bar_positions_female_unmarried = [pos + bar_width for pos in bar_positions_male_unmarried]

# Plot 'Male' and 'Female' bars for 'Unmarried'
plt.bar(bar_positions_male_unmarried, male_data['Unmarried'], width=bar_width, label='Male (Unmarried)', color='blue')
plt.bar(bar_positions_female_unmarried, female_data['Unmarried'], width=bar_width, label='Female (Unmarried)', color='pink')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Unmarried Individuals')
plt.title('Unmarried Individuals Distribution (Male and Female)')

# Set x-axis ticks and labels
ticks_positions = [pos + 0.5 * bar_width for pos in bar_positions_male_unmarried]
plt.xticks(ticks_positions, male_data['Year'])

# Show legend
plt.legend()
plt.grid(True)
# Show the plot
plt.show()


############### DIVORCED ##########################################################

import pandas as pd
import matplotlib.pyplot as plt

maritalstatus = 'maritalstatus1.xlsx'

df = pd.read_excel(maritalstatus)

# Filter data for 'Male' and 'Female'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a bar chart for 'Male' and 'Female' Divorced values
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.35

# Set the positions for the bars
bar_positions_male_divorced = range(len(male_data))
bar_positions_female_divorced = [pos + bar_width for pos in bar_positions_male_divorced]

# Plot 'Male' and 'Female' bars for 'Divorced'
plt.bar(bar_positions_male_divorced, male_data['Divorced'], width=bar_width, label='Male (Divorced)', color='lightblue')
plt.bar(bar_positions_female_divorced, female_data['Divorced'], width=bar_width, label='Female (Divorced)', color='violet')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Divorced Individuals')
plt.title('Divorced Individuals Distribution (Male and Female)')

# Set x-axis ticks and labels
ticks_positions = [pos + 0.5 * bar_width for pos in bar_positions_male_divorced]
plt.xticks(ticks_positions, male_data['Year'])

# Show legend
plt.legend()
plt.grid(True)
# Show the plot
plt.show()



############### WIDOWED ##########################################################

import pandas as pd
import matplotlib.pyplot as plt

maritalstatus = 'maritalstatus1.xlsx'

df = pd.read_excel(maritalstatus)

# Filter data for 'Male' and 'Female'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a bar chart for 'Male' and 'Female' Widowed values
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.35

# Set the positions for the bars
bar_positions_male_widowed = range(len(male_data))
bar_positions_female_widowed = [pos + bar_width for pos in bar_positions_male_widowed]

# Plot 'Male' and 'Female' bars for 'Widowed'
plt.bar(bar_positions_male_widowed, male_data['Widowed'], width=bar_width, label='Male (Widowed)', color='lightskyblue')
plt.bar(bar_positions_female_widowed, female_data['Widowed'], width=bar_width, label='Female (Widowed)', color='plum')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Widowed Individuals')
plt.title('Widowed Individuals Distribution (Male and Female)')

# Set x-axis ticks and labels
ticks_positions = [pos + 0.5 * bar_width for pos in bar_positions_male_widowed]
plt.xticks(ticks_positions, male_data['Year'])

# Show legend
plt.legend()
plt.grid(True)
# Show the plot
plt.show()





'''
################################
import pandas as pd
import matplotlib.pyplot as plt

maritalstatus = 'maritalstatus1.xlsx'

df = pd.read_excel(maritalstatus)

# Filter data for 'Male' and 'Female'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a grouped bar chart for 'Male' Unmarried, Divorced, and Widowed values
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.25

# Set the positions for the bars
bar_positions_male_unmarried = range(len(male_data))
bar_positions_male_divorced = [pos + bar_width for pos in bar_positions_male_unmarried]
bar_positions_male_widowed = [pos + 2 * bar_width for pos in bar_positions_male_unmarried]

bar_positions_female_unmarried = [pos + 3 * bar_width for pos in bar_positions_male_unmarried]
bar_positions_female_divorced = [pos + 4 * bar_width for pos in bar_positions_male_unmarried]
bar_positions_female_widowed = [pos + 5 * bar_width for pos in bar_positions_male_unmarried]

# Plot 'Male' bars for 'Unmarried', 'Divorced', and 'Widowed'
plt.bar(bar_positions_male_unmarried, male_data['Unmarried'], width=bar_width, label='Male (Unmarried)', color='blue')
plt.bar(bar_positions_male_divorced, male_data['Divorced'], width=bar_width, label='Male (Divorced)', color='lightblue')
plt.bar(bar_positions_male_widowed, male_data['Widowed'], width=bar_width, label='Male (Widowed)', color='lightskyblue')

# Plot 'Female' bars for 'Unmarried', 'Divorced', and 'Widowed'
plt.bar(bar_positions_female_unmarried, female_data['Unmarried'], width=bar_width, label='Female (Unmarried)', color='pink')
plt.bar(bar_positions_female_divorced, female_data['Divorced'], width=bar_width, label='Female (Divorced)', color='violet')
plt.bar(bar_positions_female_widowed, female_data['Widowed'], width=bar_width, label='Female (Widowed)', color='plum')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Marital Status Distribution (Male and Female)')

# Set x-axis ticks and labels
ticks_positions = [pos + 2 * bar_width for pos in bar_positions_male_unmarried]
plt.xticks(ticks_positions, male_data['Year'])

# Show legend
plt.legend()

# Show the plot
plt.show()





import pandas as pd
import matplotlib.pyplot as plt

maritalstatus = 'maritalstatus1.xlsx'

df = pd.read_excel(maritalstatus)

# Filter data for 'Male' and 'Unmarried'
male_unmarried_data = df[(df['Sex'] == 'Male') & (df['MaritalStatus'] == 'Unmarried')]
female_unmarried_data = df[(df['Sex'] == 'Female') & (df['MaritalStatus'] == 'Unmarried')]

# Reverse the order of the data
male_unmarried_data = male_unmarried_data[::-1]
female_unmarried_data = female_unmarried_data[::-1]

# Create a grouped bar chart for 'Male' and 'Female' Unmarried values
fig, ax = plt.subplots(figsize=(14, 6))

# Set the bar width
bar_width = 0.35

# Set the positions for the bars
bar_positions_male_unmarried = range(len(male_unmarried_data))
bar_positions_female_unmarried = range(len(female_unmarried_data))

# Plot 'Male' and 'Female' bars for 'Unmarried'
plt.bar(bar_positions_male_unmarried, male_unmarried_data['Count'], width=bar_width, label='Male (Unmarried)', color='blue')
plt.bar(bar_positions_female_unmarried, female_unmarried_data['Count'], width=bar_width, label='Female (Unmarried)', color='pink')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Unmarried Individuals Distribution (Male and Female)')

# Set x-axis ticks and labels
ticks_positions = [pos + bar_width/2 for pos in bar_positions_male_unmarried]
plt.xticks(ticks_positions, male_unmarried_data['Year'])

# Show legend
plt.legend()

# Show the plot
plt.show()
'''