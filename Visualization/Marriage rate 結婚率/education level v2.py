# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:17:19 2023

@author: Hao
"""

#### UNIVERSITY ##########################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

educationlevel = 'educationlevel1.xlsx'
educationlevel = os.path.join(script_dir, r'educationlevel1.xlsx')


df = pd.read_excel(educationlevel)

# Filter data for 'Male'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a line chart for 'Male' education levels
fig, ax = plt.subplots(figsize=(13, 8))

def create_line_positions(data):
    return {
        'university': range(len(data)),
    }

line_positions_male = create_line_positions(male_data)
line_positions_female = create_line_positions(female_data)

# Plot 'Male' lines for education levels with different colors
plt.plot(line_positions_male['university'], male_data['University Graduate'], marker='o', label='Male University Graduate', color='blue')
plt.plot(line_positions_female['university'], female_data['University Graduate'], marker='o', label='Female University Graduate', color='salmon')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Education Level of the Population in Taiwan years 89-110 (University level)')

# Set x-axis ticks and labels with rotation
plt.xticks(line_positions_male['university'], male_data['Year'], rotation=45, ha='right')

# Show grid lines
plt.grid(True)

# Show legend
plt.legend()

# Show the plot
plt.show()




#### DIPLOMA ##########################################################################################

import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))

educationlevel = 'educationlevel1.xlsx'
educationlevel = os.path.join(script_dir, r'educationlevel1.xlsx')


df = pd.read_excel(educationlevel)

# Filter data for 'Male'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a line chart for 'Male' education levels
fig, ax = plt.subplots(figsize=(13, 8))

def create_line_positions(data):
    return {
        'diploma': range(len(data)),
    }

line_positions_male = create_line_positions(male_data)
line_positions_female = create_line_positions(female_data)

# Plot 'Male' lines for education levels with different colors
plt.plot(line_positions_male['diploma'], male_data['Diploma'], marker='o', label='Male Diploma', color='blue')
plt.plot(line_positions_female['diploma'], female_data['Diploma'], marker='o', label='Female Diploma', color='salmon')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Education Level of the Population in Taiwan years 89-110 (Diploma)')

# Set x-axis ticks and labels with rotation
plt.xticks(line_positions_male['diploma'], male_data['Year'], rotation=45, ha='right')

# Show grid lines
plt.grid(True)

# Show legend
plt.legend()

# Show the plot
plt.show()




#### HIGH SCHOOL ##########################################################################################

import pandas as pd
import matplotlib.pyplot as plt
script_dir = os.path.dirname(os.path.abspath(__file__))

educationlevel = 'educationlevel1.xlsx'
educationlevel = os.path.join(script_dir, r'educationlevel1.xlsx')

df = pd.read_excel(educationlevel)

# Filter data for 'Male'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a line chart for 'Male' education levels
fig, ax = plt.subplots(figsize=(13, 8))

def create_line_positions(data):
    return {
        'High School Graduate': range(len(data)),
    }

line_positions_male = create_line_positions(male_data)
line_positions_female = create_line_positions(female_data)

plt.plot(line_positions_male['High School Graduate'], male_data['High School Graduate'], marker='o', label='Male High School Graduate', color='blue')
plt.plot(line_positions_female['High School Graduate'], female_data['High School Graduate'], marker='o', label='Female High School Graduate', color='salmon')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Education Level of the Population in Taiwan years 89-110 (High School level)')

# Set x-axis ticks and labels with rotation
plt.xticks(line_positions_male['High School Graduate'], male_data['Year'], rotation=45, ha='right')

# Show grid lines
plt.grid(True)

# Show legend
plt.legend()

# Show the plot
plt.show()



#### JUNIOR HIGH GRADUATE ##########################################################################################

import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))

educationlevel = 'educationlevel1.xlsx'
educationlevel = os.path.join(script_dir, r'educationlevel1.xlsx')

df = pd.read_excel(educationlevel)

# Filter data for 'Male'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a line chart for 'Male' education levels
fig, ax = plt.subplots(figsize=(13, 8))

line_positions_male_junior_high = range(len(male_data))
line_positions_female_junior_high = range(len(female_data))

# Plot 'Male' lines for education levels with different colors
plt.plot(line_positions_male_junior_high, male_data['Junior High Graduate'], marker='o', label='Male Junior High Graduate', color='blue')
plt.plot(line_positions_female_junior_high, female_data['Junior High Graduate'], marker='o', label='Female Junior High Graduate', color='salmon')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Education Level of the Population in Taiwan years 89-110 (Junior High Level)')

# Set x-axis ticks and labels with rotation
plt.xticks(line_positions_male_junior_high, male_data['Year'], rotation=45, ha='right')

# Show grid lines
plt.grid(True)

# Show legend
plt.legend()

# Show the plot
plt.show()


#### Elemental School Graduate ##########################################################################################

import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))

educationlevel = 'educationlevel1.xlsx'
educationlevel = os.path.join(script_dir, r'educationlevel1.xlsx')

df = pd.read_excel(educationlevel)

# Filter data for 'Male'
male_data = df[df['Sex'] == 'Male']
female_data = df[df['Sex'] == 'Female']

# Reverse the order of the data
male_data = male_data[::-1]
female_data = female_data[::-1]

# Create a line chart for 'Male' education levels
fig, ax = plt.subplots(figsize=(13, 8))

line_positions_male_elementary = range(len(male_data))
line_positions_female_elementary = range(len(female_data))

# Plot 'Male' lines for education levels with different colors
plt.plot(line_positions_male_elementary, male_data['Elemental School Graduate'], marker='o', label='Male Elemental School Graduate', color='blue')
plt.plot(line_positions_female_elementary, female_data['Elemental School Graduate'], marker='o', label='Female Elemental School Graduate', color='salmon')

# Set labels and title
plt.xlabel('Years')
plt.ylabel('Number of Individuals')
plt.title('Education Level of the Population in Taiwan years 89-110 (Elementary School Level)')

# Set x-axis ticks and labels with rotation
plt.xticks(line_positions_male_elementary, male_data['Year'], rotation=45, ha='right')

# Show grid lines
plt.grid(True)

# Show legend
plt.legend()

# Show the plot
plt.show()

