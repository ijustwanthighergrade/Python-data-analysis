# -*- coding: utf-8 -*-
import os
import io
import base64
import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
import mpld3

script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the Excel file
maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')
script_dir = os.path.dirname(os.path.abspath(__file__))
totalmarriages = os.path.join(script_dir, r'data\number_of_marriages1.xlsx')

def home(request):
    c = {}
    c['birthrate'] = birthrate_to_base64()
    
    c['housepriceindex'] = housepriceindex_to_base64()
    
    c['age'] =age_to_base64()
    
    c['educationlevelM'] =educationlevelM_to_base64()
    c['educationlevelF'] =educationlevelF_to_base64()
    c['educationlevelTotlePieChart'] =educationlevelTotlePieChart_to_base64()
    
    c['maritalstatusM'] =maritalstatusM_to_base64()
    c['maritalstatusF'] =maritalstatusF_to_base64()
    c['maritalstatusPIECHART'] =maritalstatusPIECHART_to_base64()
    
    c['totalmarriagesnumber'] =totalmarriagesnumber_to_base64()
    c['totalmarriagesnumberF'] =totalmarriagesnumberF_to_base64()
    c['totalmarriagesnumberM'] =totalmarriagesnumberM_to_base64()
    c['totalmarriagesPIECHART'] =totalmarriagesPIECHART_to_base64()

    return render(request, 'home/home.html', c)

def analysis(request):

    return render(request, 'home/analysis.html')

# The graph in home
def birthrate():
    birthrate1 = 'birthrate1.xlsx'
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    birthrate1 = os.path.join(script_dir, 'data/birthrate1.xlsx')

    # Read the Excel file
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

    # Do not show the plot here

    # Return the Matplotlib figure
    return fig

def housepriceindex():
    housepriceindex = 'housepriceindex1.xlsx'
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    housepriceindex = os.path.join(script_dir, 'data/housepriceindex1.xlsx')
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

    # Set x-axis ticks and labels
    plt.xticks(line_positions, df['Annual season'])

    # Return the Matplotlib figure
    return fig

def age():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    age = os.path.join(script_dir, 'data/age1.xlsx')

    file = pd.read_excel(age)

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

    fig=plt.figure(figsize=(10, 8))  # Set the figure size

    plt.pie(
        [total_under_15, total_15_19, total_20_24, total_25_29, total_30_34, total_35_39, total_40_44, total_45_49, total_50_54, total_55_59, total_60_64, total_over_65],
        labels=['Under 15 years old', '15-19 years old', '20-24 years old', '25-29 years old', '30-34 years old', '35-39 years old', '40-44 years old', '45-49 years old', '50-54 years old', '55-59 years old', '60-64 years old', 'Over 65 years old'],
        autopct='%1.1f%%',
        explode=explode  # Increase the distance between slices
    )

    plt.title('Total Average Number of Marriages divided by age from years 89 - 110')
    return fig

def educationlevelM():
    script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the Excel file
    educationlevel = os.path.join(script_dir, 'data\educationlevel1.xlsx')

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
    return fig

def educationlevelF():
    script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the Excel file
    educationlevel = os.path.join(script_dir, 'data\educationlevel1.xlsx')

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
    return fig

def educationlevelTotlePieChart():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    educationlevel = os.path.join(script_dir, 'data/educationlevel1.xlsx')

    file = pd.read_excel(educationlevel)

    # Filter data for 'Male' and 'Female'
    male_data = file[file['Sex'] == 'Male']
    female_data = file[file['Sex'] == 'Female']

    # Calculate total values for 'Male' and 'Female'
    total_male = male_data['Total'].sum()
    total_female = female_data['Total'].sum()

    # Plotting the pie chart for 'Male' and 'Female'
    fig=plt.figure(figsize=(10, 8))
    plt.pie([total_male, total_female], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
    plt.title('Education Level of Male and Female Population in Taiwan from years 89-110')
    return fig

def maritalstatusM():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')

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
    return fig

def maritalstatusF():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the Excel file
    maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')

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
    return fig

def maritalstatusPIECHART():
    script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the Excel file
    maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')

    file = pd.read_excel(maritalstatus)

    # Filter data for 'Male' and 'Female'
    male_data = file[file['Sex'] == 'Male']
    female_data = file[file['Sex'] == 'Female']

    # Calculate total values for 'Male' and 'Female'
    total_male = male_data['Total'].sum()
    total_female = female_data['Total'].sum()

    fig =plt.figure(figsize=(10, 8))  # Set the figure size

    # Set colors for 'Male' and 'Female'
    colors = ['lightblue', 'pink']

    plt.pie(
        [total_male, total_female],
        labels=['Male', 'Female'],
        autopct='%1.1f%%',
        colors=colors  # Set colors for each slice
    )

    plt.title('Total of out-of-marriage males and females from years 89-110')

    return fig

def totalmarriagesPIECHART():
    file = pd.read_excel(totalmarriages)

    # Extract relevant data for 'First Marriage' and 'Remarriage'
    First_marriage = file['First Marriage'].sum()
    Remarriage = file['Remarriage'].sum()


    fig=plt.figure(figsize=(10, 8))  # Set the figure size

    plt.pie(
        [First_marriage, Remarriage],
        labels=['First Marriage', 'Remarriage'],
        autopct='%1.1f%%',
    )

    plt.title('Total Number of Marriages years 89 - 110')
    return fig

def totalmarriagesnumber():
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
    return fig

def totalmarriagesnumberF():
    file = pd.read_excel(totalmarriages)

    # Filter data for 'Female'
    female_data = file[file['Sex'] == 'Female']

    # Extract relevant data for 'First Marriage' and 'Remarriage'
    First_marriage = female_data['First Marriage'].sum()
    Remarriage = female_data['Remarriage'].sum()

    fig=plt.figure(figsize=(10, 8))  # Set the figure size

    colors = ['pink', 'violet']

    plt.pie(
        [First_marriage, Remarriage],
        labels=['First Marriage', 'Remarriage'],
        autopct='%1.1f%%',
        colors=colors
    )

    plt.title('Total Number of Marriages (Female) years 89 - 110')

    return fig
def totalmarriagesnumberM():
    file = pd.read_excel(totalmarriages)

    # Filter data for 'Male'
    Male_data = file[file['Sex'] == 'Male']

    # Extract relevant data for 'First Marriage' and 'Remarriage'
    First_marriage = Male_data['First Marriage'].sum()
    Remarriage = Male_data['Remarriage'].sum()

    fig=plt.figure(figsize=(10, 8))  # Set the figure size

    colors = ['lightblue', 'skyblue']

    plt.pie(
        [First_marriage, Remarriage],
        labels=['First Marriage', 'Remarriage'],
        autopct='%1.1f%%',
        colors=colors
    )

    plt.title('Total Number of Marriages (Male) years 89 - 110')

    return fig

def fig_to_base64(fig):
    # Convert the Matplotlib figure to base64
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    data_uri = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Create the data URI for the image
    img_tag = f'<img class="graph" src="data:image/png;base64,{data_uri}" alt="Matplotlib Chart"/>'
    return img_tag

def birthrate_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = birthrate()

    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)

    return img_tag
def housepriceindex_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = housepriceindex()

    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)

    return img_tag
def age_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = age()

    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)

    return img_tag

def educationlevelM_to_base64():
    fig = educationlevelM()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

def educationlevelF_to_base64():
    fig = educationlevelF()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

def educationlevelTotlePieChart_to_base64():
    fig = educationlevelTotlePieChart()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

def maritalstatusM_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = maritalstatusM()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

def maritalstatusF_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = maritalstatusF()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

def maritalstatusPIECHART_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = maritalstatusPIECHART()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

def totalmarriagesPIECHART_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = totalmarriagesPIECHART()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

def totalmarriagesnumber_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = totalmarriagesnumber()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag
def totalmarriagesnumberF_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = totalmarriagesnumberF()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag
def totalmarriagesnumberM_to_base64():
    # Call the birthrate function to get the Matplotlib figure
    fig = totalmarriagesnumberM()
    # Convert the Matplotlib figure to base64
    img_tag = fig_to_base64(fig)
    return img_tag

