# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:03:41 2023

@author: Hao
"""

#####################################
##### EDUCATION LEVEL MALES ################################################
#####################################

import pandas as pd
import matplotlib.pyplot as plt

educationlevel = 'educationlevel1.xlsx'

df = pd.read_excel(educationlevel)

# Filter data for 'Male'
male_data = df[df['Sex'] == 'Male']

# Reverse the order of the data
male_data = male_data[::-1]

# Create a line chart for 'Male' education levels
fig, ax = plt.subplots(figsize=(13, 8))

# Set the positions for the lines
line_positions_male_university = range(len(male_data))
line_positions_male_diploma = [pos for pos in line_positions_male_university]
line_positions_male_high_school = [pos for pos in line_positions_male_university]
line_positions_male_junior_high = [pos for pos in line_positions_male_university]
line_positions_male_elementary = [pos for pos in line_positions_male_university]

# Plot 'Male' lines for education levels with different colors
plt.plot(line_positions_male_university, male_data['University Graduate'], marker='o', label='University Graduate', color='brown')
plt.plot(line_positions_male_diploma, male_data['Diploma'], marker='o', label='Diploma', color='gold')
plt.plot(line_positions_male_high_school, male_data['Graduated High School'], marker='o', label='Graduated High School', color='teal')
plt.plot(line_positions_male_junior_high, male_data['Graduated Junior High'], marker='o', label='Graduated Junior High', color='darkorchid')
plt.plot(line_positions_male_elementary, male_data['Graduated Elementary School'], marker='o', label='Graduated Elementary School', color='sienna')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Education Level of the Male Population in Taiwan years 89-110')

# Set x-axis ticks and labels
plt.xticks(line_positions_male_university, male_data['Year'])

# Show legend
plt.legend()

# Show the plot
plt.show()




#####################################
##### EDUCATION LEVEL FEMALES ################################################
#####################################

import pandas as pd
import matplotlib.pyplot as plt

educationlevel = 'educationlevel1.xlsx'

df = pd.read_excel(educationlevel)

# Filter data for 'Female'
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
female_data = female_data[::-1]

# Create a line chart for 'Female' education levels
fig, ax = plt.subplots(figsize=(13, 8))

# Set the positions for the lines
line_positions_female_university = range(len(female_data))
line_positions_female_diploma = [pos for pos in line_positions_female_university]
line_positions_female_high_school = [pos for pos in line_positions_female_university]
line_positions_female_junior_high = [pos for pos in line_positions_female_university]
line_positions_female_elementary = [pos for pos in line_positions_female_university]

# Plot 'Female' lines for education levels with distinct colors
plt.plot(line_positions_female_university, female_data['University Graduate'], marker='o', label='University Graduate', color='orange')
plt.plot(line_positions_female_diploma, female_data['Diploma'], marker='o', label='Diploma', color='green')
plt.plot(line_positions_female_high_school, female_data['Graduated High School'], marker='o', label='Graduated High School', color='blue')
plt.plot(line_positions_female_junior_high, female_data['Graduated Junior High'], marker='o', label='Graduated Junior High', color='purple')
plt.plot(line_positions_female_elementary, female_data['Graduated Elementary School'], marker='o', label='Graduated Elementary School', color='red')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Education Level of the Female Population in Taiwan years 89-110')

# Set x-axis ticks and labels
plt.xticks(line_positions_female_university, female_data['Year'])

# Show legend
plt.legend()

# Show the plot
plt.show()


#####################################
##### EDUCATION LEVEL TOTAL PIE CHART ################################################
#####################################

import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel('educationlevel1.xlsx')

# Filter data for 'Male' and 'Female'
male_data = file[file['Sex'] == 'Male']
female_data = file[file['Sex'] == 'Female']

# Calculate total values for 'Male' and 'Female'
total_male = male_data['Total'].sum()
total_female = female_data['Total'].sum()

# Plotting the pie chart for 'Male' and 'Female'
plt.figure(figsize=(10, 8))
plt.pie([total_male, total_female], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
plt.title('Education Level of Male and Female Population in Taiwan from years 89-110')

# Show the plot
plt.show()


#print("Male Unique Values:", male_data['Total'].unique())
#print("Female Unique Values:", female_data['Total'].unique())
