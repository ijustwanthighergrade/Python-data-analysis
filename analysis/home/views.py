# -*- coding: utf-8 -*-
import os
import io
import base64
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
from django.shortcuts import render
import mpld3
from home.models import MarriageSurvey
from apyori import apriori

script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the Excel file
maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')
totalmarriages = os.path.join(script_dir, r'data\number_of_marriages1.xlsx')

educationlevel = os.path.join(script_dir, r'data\educationlevel1.xlsx')
file_path = os.path.join(script_dir, r'data\income1.xlsx')

def home(request):
    c = {}
    c['birthrate'] = birthrate()
    
    c['housepriceindex'] = housepriceindex()
    
    c['age'] =age()
    
    c['educationlevelUNIVERSITY'] =UNIVERSITY()
    c['educationlevelDIPLOMA'] =DIPLOMA()
    c['educationlevelHIGHSCHOOL'] =HIGHSCHOOL()
    c['educationlevelJUNIORHIGH'] =JUNIORHIGH()
    c['educationlevelElemental'] =Elemental()
    c['educationlevelTotlePieChart'] =educationlevelTotlePieChart()
    
    # c['maritalstatusPIECHART'] =maritalstatusPIECHART()
    c['maritalstatusUNMARRIED'] =maritalstatusUNMARRIED()
    c['maritalstatusDIVORCED'] =maritalstatusDIVORCED()
    c['maritalstatusWIDOWED'] =maritalstatusWIDOWED()

    
    c['totalmarriagesnumber'] =totalmarriagesnumber()
    c['totalmarriagesnumberF'] =totalmarriagesnumberF()
    c['totalmarriagesnumberM'] =totalmarriagesnumberM()
    c['totalmarriagesPIECHART'] =totalmarriagesPIECHART()
    
    #income
    c['incomeMidtermpopulation'] =incomeMidtermpopulation()
    c['incomeAverageexchangerate'] =incomeAverageexchangerate()
    c['incomeEconomicgrowthrate'] =incomeEconomicgrowthrate()
    c['incomeGDP'] =incomeGDP()
    c['incomeAverageGDP'] =incomeAverageGDP()
    c['incomeGNI'] =incomeGNI()
    c['incomeAverageGNI'] =incomeAverageGNI()
    c['incomeNational'] =incomeNational()
    c['incomeAverageperson'] =incomeAverageperson()

    return render(request, 'home/home.html', c)

def analysis(request):
    survey_data = MarriageSurvey.objects.all()
    data_list = []
    for survey in survey_data:
        survey_data = {
            'timestamp': survey.timestamp,
            'gender': survey.gender,
            'education': survey.education,
            'age': survey.age,
            'salary': survey.salary,
            'is_married': survey.is_married,
            'marriage_intention': survey.marriage_intention,
            'agree_buying_house': survey.agree_buying_house,
            'buying_house_influence': survey.buying_house_influence,
            'marriage_house_requirement': survey.marriage_house_requirement,
            'afford_house_price': survey.afford_house_price,
            'buying_house_impact_life': survey.buying_house_impact_life,
            'government_support': survey.government_support,
            'family_planning': survey.family_planning,
            'desire_for_children': survey.desire_for_children,
            'legal_recognition': survey.legal_recognition,
            'tradition': survey.tradition,
            'responsibility_sharing': survey.responsibility_sharing,
            'sacrifice_lifestyle': survey.sacrifice_lifestyle,
            'affordability': survey.affordability,
            'marriage_expenses_affordability': survey.marriage_expenses_affordability,
            'stable_career_before_family': survey.stable_career_before_family,
            'child_rearing_cost_affordability': survey.child_rearing_cost_affordability,
            'non_economic_factor_relationship': survey.non_economic_factor_relationship,
            'family_adjustment_concerns': survey.family_adjustment_concerns,
            'trustworthiness': survey.trustworthiness,
            'fear_of_commitment': survey.fear_of_commitment,
            'freedom_loss_after_marriage': survey.freedom_loss_after_marriage,
            'no_partner': survey.no_partner,
            'fear_of_marriage_failure': survey.fear_of_marriage_failure,
            'anycommond': survey.anycommond,
        }
        data_list.append(survey_data)  
    alliwanttoshow={}
    alliwanttoshow['data_list']=data_list
    # print(alliwanttoshow['data_list'])
    return render(request, 'home/analysis.html',alliwanttoshow)

# The graph in home
def birthrate():
    birthrate1 = 'birthrate1.xlsx'
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    birthrate1 = os.path.join(script_dir, 'data/birthrate1.xlsx')

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
    fig = fig_to_base64(fig)

    return fig

def housepriceindex():
    housepriceindex = 'housepriceindex1.xlsx'
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    housepriceindex = os.path.join(script_dir, 'data/housepriceindex1.xlsx')
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

    fig = fig_to_base64(fig)

    # Return the Matplotlib figure
    return fig

def age():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    age = os.path.join(script_dir, 'data/age1.xlsx')

    file = pd.read_excel(age)

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
    fig = fig_to_base64(fig)

    return fig
def DIPLOMA():
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
    plt.title('Education Level of the Male Population in Taiwan years 89-110 (Diploma)')

    # Set x-axis ticks and labels with rotation
    plt.xticks(line_positions_male['diploma'], male_data['Year'], rotation=45, ha='right')

    # Show grid lines
    plt.grid(True)

    # Show legend
    plt.legend()
    fig = fig_to_base64(fig)
    return fig

def UNIVERSITY():
   
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
    plt.title('Education Level of the Male Population in Taiwan years 89-110 (University level)')

    # Set x-axis ticks and labels with rotation
    plt.xticks(line_positions_male['university'], male_data['Year'], rotation=45, ha='right')

    # Show grid lines
    plt.grid(True)

    # Show legend
    plt.legend()
    fig = fig_to_base64(fig)
    return fig

def HIGHSCHOOL():
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
    plt.title('Education Level of the Male Population in Taiwan years 89-110 (High School level)')

    # Set x-axis ticks and labels with rotation
    plt.xticks(line_positions_male['High School Graduate'], male_data['Year'], rotation=45, ha='right')

    # Show grid lines
    plt.grid(True)

    # Show legend
    plt.legend()
    fig = fig_to_base64(fig)
    return fig

def JUNIORHIGH():
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
    plt.title('Education Level of the Male Population in Taiwan years 89-110 (Junior High Level)')

    # Set x-axis ticks and labels with rotation
    plt.xticks(line_positions_male_junior_high, male_data['Year'], rotation=45, ha='right')

    # Show grid lines
    plt.grid(True)

    # Show legend
    plt.legend()
    fig = fig_to_base64(fig)
    return fig

def Elemental():
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
    plt.title('Education Level of the Male Population in Taiwan years 89-110 (Elementary School Level)')

    # Set x-axis ticks and labels with rotation
    plt.xticks(line_positions_male_elementary, male_data['Year'], rotation=45, ha='right')

    # Show grid lines
    plt.grid(True)

    # Show legend
    plt.legend()
    fig = fig_to_base64(fig)
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
    fig = fig_to_base64(fig)
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
    
    fig = fig_to_base64(fig)
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
    
    
    fig = fig_to_base64(fig)
    return fig

def maritalstatusUNMARRIED():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the Excel file
    maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')

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
    
    fig = fig_to_base64(fig)
    return fig

def maritalstatusDIVORCED():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the Excel file
    maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')

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
        
    fig = fig_to_base64(fig)
    return fig

def maritalstatusWIDOWED():
    script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the Excel file
    maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')

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
    fig = fig_to_base64(fig)
    return fig

# def maritalstatusPIECHART():
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

    fig = fig_to_base64(fig)
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
    
    fig = fig_to_base64(fig)
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
    
    fig = fig_to_base64(fig)
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

    fig = fig_to_base64(fig)
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

    fig = fig_to_base64(fig)
    return fig

def incomeMidtermpopulation():
    df = pd.read_excel(file_path)

    # Assuming 'Midterm population (person)' is the new midterm population column name
    midterm_population_column = 'Midterm population (person)'

    # Create a line plot for Midterm population
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[midterm_population_column], label='Midterm population (person)', marker='o')  # Plot Midterm population

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Midterm Population over the years Taiwan years 80-110')
    plt.xlabel('Statistical Period')
    plt.ylabel('Population in millions')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeAverageexchangerate():
    df = pd.read_excel(file_path)

    # Assuming 'Average exchange rate (yuan/USD)' is the new average exchange rate column name
    average_exchange_rate_column = 'Average exchange rate (yuan/USD)'

    # Create a line plot for Average exchange rate with purple color
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[average_exchange_rate_column], label='Average exchange rate (yuan/USD)', marker='o', color='purple')  # Plot Average exchange rate

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Average Exchange Rate over the years Taiwan years 80-110')
    plt.xlabel('Statistical Period')
    plt.ylabel('Exchange Rate (yuan/USD)')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeEconomicgrowthrate():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Economic growth rate (%)' is the new economic growth rate column name
    economic_growth_rate_column = 'Economic growth rate (%)'

    # Create a line plot for Economic growth rate
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[economic_growth_rate_column], label='Economic growth rate (%)', marker='o', color='gold')  # Plot Economic growth rate

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Economic Growth Rate over the years Taiwan years 80-110')
    plt.xlabel('Statistical Period')
    plt.ylabel('Growth Rate (%)')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeGDP():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

        # Assuming 'Gross domestic product GDP (nominal value, million yuan)' is the GDP column name
    gdp_column = 'Gross domestic product GDP (nominal value, million yuan)'

    # Create a line plot for GDP only
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[gdp_column], label='Gross domestic product GDP (nominal value, million yuan)', marker='o', color='brown')  # Plot GDP

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Income over the years Taiwan years 80-110 (Gross Domestic Product GDP)')
    plt.xlabel('Statistical Period')
    plt.ylabel('Amount in Millions yuan')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeAverageGDP():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

        # Assuming 'Average GDP per capita (nominal value, yuan)' is the new GDP column name
    gdp_column = 'Average GDP per capita (nominal value, yuan)'

    # Create a line plot for Average GDP per capita
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[gdp_column], label='Average GDP per capita (nominal value, yuan)', marker='o', color='red')  # Plot Average GDP per capita

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Income over the years Taiwan years 80-110 (Average GDP per capita)')
    plt.xlabel('Statistical Period')
    plt.ylabel('Amount in Yuan')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeGNI():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Gross national income GNI (nominal value, million yuan)' is the new GNI column name
    gni_column = 'Gross national income GNI (nominal value, million yuan)'

    # Create a line plot for Gross national income GNI
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[gni_column], label='Gross national income GNI (nominal value, million yuan)', marker='o', color='skyblue')  # Plot GNI

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Income over the years Taiwan years 80-110 (Gross National Income GNI)')
    plt.xlabel('Statistical Period')
    plt.ylabel('Amount in Millions yuan')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeAverageGNI():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Average GNI per person (nominal value, yuan)' is the new GNI per person column name
    gni_per_person_column = 'Average GNI per person (nominal value, yuan)'

    # Create a line plot for Average GNI per person
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[gni_per_person_column], label='Average GNI per person (nominal value, yuan)', marker='o', color='green')  # Plot Average GNI per person

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Income over the years Taiwan years 80-110 (Average GNI per person)')
    plt.xlabel('Statistical Period')
    plt.ylabel('Amount in Yuan')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeNational():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'National income (nominal value, million yuan)' is the new national income column name
    national_income_column = 'National income (nominal value, million yuan)'

    # Create a line plot for National income
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[national_income_column], label='National income (nominal value, million yuan)', marker='o', color='grey')  # Plot National income

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Income over the years Taiwan years 80-110 (National Income)')
    plt.xlabel('Statistical Period')
    plt.ylabel('Amount in Millions yuan')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
    return fig

def incomeAverageperson():
    df = pd.read_excel(file_path)

    # Assuming 'Average income per person (nominal value, yuan)' is the new average income per person column name
    average_income_per_person_column = 'Average income per person (nominal value, yuan)'

    # Create a line plot for Average income per person
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(df[average_income_per_person_column], label='Average income per person (nominal value, yuan)', marker='o', color='slateblue')  # Plot Average income per person

    # Set x-axis ticks using reversed order of Statistical Periods
    plt.xticks(range(len(df)), reversed(df['Statistical Period']), rotation=45, ha='right')

    plt.title('Income over the years Taiwan years 80-110 (Average Income per person)')
    plt.xlabel('Statistical Period')
    plt.ylabel('Amount in Yuan')
    plt.legend()  # Display legend
    plt.grid(True)  # Display grid
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    fig = fig_to_base64(fig)
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

