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
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import django
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.http import JsonResponse
from django.db.models import Q
import numpy as np
from collections import defaultdict
from collections import OrderedDict
import json

# 設定字型，使用支援中文的字型（例如 Microsoft JhengHei）
rcParams['font.sans-serif'] = ['Microsoft JhengHei']

# 顯示全形字符警告
rcParams['axes.unicode_minus'] = False
script_dir = os.path.dirname(os.path.abspath(__file__))

maritalstatus = os.path.join(script_dir, 'data\maritalstatus1.xlsx')
totalmarriages = os.path.join(script_dir, r'data\number_of_marriages1.xlsx')
educationlevel = os.path.join(script_dir, r'data\educationlevel1.xlsx')
file_path = os.path.join(script_dir, r'data\income1.xlsx')

# The page to show Data Visualization
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

def analysis(request: HttpRequest):
    importdata()
    alliwanttoshow={}
    alliwanttoshow['kmeansAgeIntention']=kmeansAgeIntention()
    
    alliwanttoshow['gender']=['男','女']
    alliwanttoshow['education_levels'] = ['小學','國中','高中','大學','碩士','博士']
    alliwanttoshow['age'] = [
    '17歲(含)以下',
    '18～20',
    '21～29',
    '30～39',
    '40～49',
    '50～59',
    '60～69',
    '70～79',
    '80～89',
    '90以上']
    alliwanttoshow['income'] = [
    '0～19999',
    '20000～39999',
    '40000～59999',
    '60000~79999',
    '80000~99999',
    '100000~119000',
    '120000～139999',
    '140000以上',
    '家管',
    '學生無收入'
    ]
    alliwanttoshow['marriageornot']=["是","否"]
    alliwanttoshow['column_names'] = ["時間戳記", "生理性別", "最高學歷", "您的年齡", "目前月薪資水平(台幣)", "您是否已婚？", "您目前是否有結婚意願(不論單身與否)",
     "您認同買房是影響多數人結婚的重要因素嗎？", "請問買房影響您結婚意願的程度為？", "您對結婚一定得買房的認同度為何？",
     "請問您認為自己目前薪資能獨自負擔逐年攀升的房價的程度為？", "您認同買房會影響到個人生活水平的程度為？",
     "您認為政府在買房上已擁有完善配套措施的程度為？", "想要與心愛的人共組家庭", "想要小孩", "想要讓伴侶關係被法律所認同",
     "傳統上結婚是人生的必經之路", "想要伴侶一同承擔責任", "不想因為結婚犧牲現有生活水平", "無法負擔高額房價", "無法負擔結婚開銷",
     "想要先穩定事業再組建家庭", "無法負擔子女教養費用", "只需要情感需求，不想綁定法律義務", "害怕要與對方家庭磨合", "不知是否對方值得信任",
     "不想養小孩", "婚後會失去自由", "沒有對象", "害怕婚姻失敗", "任何指教"]
    alliwanttoshow['data_list']=[]
    alliwanttoshow['optionalnum']=[1,2,3,4,5]
    allofdata=getalldata()
    allofdatanum=len(allofdata)
    dictfordatalist={}
    
    
    jsonf = os.path.join(script_dir, r'C:\Users\DAIYUNWU\Desktop\Python-data-analysis\analysis\outputtest.json')
    with open(jsonf, 'r') as json_file:
            data = json.load(json_file)
    alliwanttoshow['json']=data
    
    if request.GET.get('selected_option'):
        selected_option = request.GET.get('selected_option')
        html=""
        # Extracting optgroup and option
        if selected_option:
            optgroup, option = selected_option.split(':')
            alliwanttoshow['data_list']=filiterdata(optgroup,option)
            filiterdatanum=len(alliwanttoshow['data_list'])
            alliwanttoshow['html']=f"<p class='optgroup'>Optgroup: {optgroup}</p>"
            alliwanttoshow['html']+=f"<p class='option'>Option: {option}</p>"
            alliwanttoshow['html']+=f"<p class='filtered-data'>Filtered Data Number: {filiterdatanum}</p>"
            alliwanttoshow['html']+=f"<p class='ratio'>Ratio of all data: {round(filiterdatanum/allofdatanum*100,4)}%</p>"
            dictfordatalist=count_results(alliwanttoshow['data_list'])
            alliwanttoshow['barchart']=create_bar_chart(dictfordatalist)
            
        return JsonResponse(alliwanttoshow)
    else:
        alliwanttoshow['data_list']=allofdata
        dictfordatalist=count_results(alliwanttoshow['data_list'])
        alliwanttoshow['barchart']=create_bar_chart(dictfordatalist)
        alliwanttoshow['data_num']=allofdatanum
        # print(alliwanttoshow['barchart'])
        return render(request, 'home/analysis.html',alliwanttoshow)
def count_results(allofdata):
    count_results = defaultdict(OrderedDict)
    for respondent in allofdata:
        for series, response in respondent.items():
            count_results[series][response] = count_results[series].get(response, 0) + 1
    return count_results

def apriori(request):
    alliwanttoshow={}
    jsonf = os.path.join(script_dir, r'C:\Users\DAIYUNWU\Desktop\Python-data-analysis\analysis\outputtest.json')
    with open(jsonf, 'r') as json_file:
            data = json.load(json_file)
    alliwanttoshow['json']=data
    return render(request, 'home/apriori.html',alliwanttoshow)

def getalldata():
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
    return data_list

def filiterdata(optgroup,option):
    query = Q(**{f"{optgroup}__exact": option})
    survey_data = MarriageSurvey.objects.filter(query)
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
    
    return data_list

lista=['gender', 'education', 'age', 'salary', 'is_married',
       'marriage_intention', 'agree_buying_house', 'buying_house_influence',
       'marriage_house_requirement', 'afford_house_price',
       'buying_house_impact_life', 'government_support', 'family_planning',
       'desire_for_children', 'legal_recognition', 'tradition',
       'responsibility_sharing', 'sacrifice_lifestyle', 'affordability',
       'marriage_expenses_affordability', 'stable_career_before_family',
       'child_rearing_cost_affordability', 'non_economic_factor_relationship',
       'family_adjustment_concerns', 'trustworthiness', 'fear_of_commitment',
       'freedom_loss_after_marriage', 'no_partner',
       'fear_of_marriage_failure']
listb=["生理性別", "最高學歷", "您的年齡", "目前月薪資水平(台幣)", "您是否已婚？",
            '您目前是否有結婚意願(不論單身與否)\n已婚者可以是否後悔結婚來考量', '您認同買房是影響多數人結婚的重要因素嗎？', '請問買房影響您結婚意願的程度為？', 
             '您對結婚一定得買房的認同度為何？', '請問您認為自己目前薪資能獨自負擔逐年攀升的房價的程度為？', '您認同買房會影響到個人生活水平的程度為？', 
             '您認為政府在買房上已擁有完善配套措施的程度為？', '可能使擁有結婚意願的因素：想要與心愛的人共組家庭', '可能使擁有結婚意願的因素：想要小孩', 
             '可能使擁有結婚意願的因素：想要讓伴侶關係被法律所認同', '可能使擁有結婚意願的因素：傳統上結婚是人生的必經之路', 
             '可能使擁有結婚意願的因素：想要伴侶一同承擔責任', '可能影響您結婚意願的經濟因素：不想因為結婚犧牲現有生活水平', 
             '可能影響您結婚意願的經濟因素：無法負擔高額房價', '可能影響您結婚意願的經濟因素：無法負擔結婚開銷', 
             '可能影響您結婚意願的經濟因素：想要先穩定事業再組建家庭', '可能影響您結婚意願的經濟因素：無法負擔子女教養費用', 
             '可能影響您結婚意願的非經濟因素：只需要情感需求，不想綁定法律義務', '可能影響您結婚意願的非經濟因素：害怕要與對方家庭磨合', 
             '可能影響您結婚意願的非經濟因素：不知是否對方值得信任', '可能影響您結婚意願的非經濟因素：不想養小孩', 
             '可能影響您結婚意願的非經濟因素：婚後會失去自由', '可能影響您結婚意願的非經濟因素：沒有對象', '可能影響您結婚意願的非經濟因素：害怕婚姻失敗']
dictforlebal={}

dictforlebalname={'可能使擁有結婚意願的因素':1,'可能影響您結婚意願的經濟因素':2,'可能影響您結婚意願的非經濟因素':3}

for i in range(len(lista)):
    dictforlebal[lista[i]]=listb[i]
# print(dictforlebal)
def create_bar_chart(data):
    allofchart=[]
    before_special_field = True
    macaron_colors = [
        "#ffd9e1", "#99ccff", "#98fb98", "#ddbbff", "#9cfcf9",
        "#ffcc99", "#4888db", "#75d0ba", "#3b8265", "#ffdb58",
        "#f0e68c", "#890f51", "#73114e", "#5c0e46", "#480c3e",
        "#360934", "#24062b", "#14031d", "#08000d", "#000000"
    ]
    for i,(series, counts) in enumerate(data.items()):
        options = list(counts.keys())
        counts_values = list(counts.values())
        special_field = 'marriage_intention'
        if series== special_field:
            before_special_field = False

        if i == 0 or i == len(data) - 1:
            continue
        
        if before_special_field:
            fig, ax = plt.subplots(figsize=(8, 8))
            selectedcolumn = dictforlebal.get(series)

            # 為每個扇形手動設置顏色
            patches, texts, autotexts = ax.pie(counts_values, labels=options, autopct='%1.1f%%', startangle=90)
            for i, patch in enumerate(patches):
                patch.set_facecolor(macaron_colors[i])
                
            plt.title(selectedcolumn)
            fig=fig_to_base64(fig)
            allofchart.append(fig)
        else:
            
            numcolor=0
            selectedcolumn = dictforlebal.get(series)
            if '：' in selectedcolumn:
                value, column = selectedcolumn.split('：')
                numcolor =dictforlebalname.get(value)
                
            fig=plt.figure(figsize=(10, 6))
            bars =plt.bar(options, counts_values, color=macaron_colors[numcolor])
            plt.xlabel('Options')
            plt.ylabel('Number of People')
            plt.title(selectedcolumn)
            plt.bar_label(bars, labels=counts_values)

            fig=fig_to_base64(fig)
            allofchart.append(fig)
    return allofchart



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
    plt.title('Education Level of the Population in Taiwan years 89-110 (Diploma)')

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
    plt.title('Education Level of the Population in Taiwan years 89-110 (University level)')

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
    plt.title('Education Level of the Population in Taiwan years 89-110 (High School level)')

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
    plt.title('Education Level of the Population in Taiwan years 89-110 (Junior High Level)')

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
    plt.title('Education Level of the Population in Taiwan years 89-110 (Elementary School Level)')

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

    # Assuming 'Population (person)' is the new population column name
    population_column = 'Population (person)'

    # Create a line plot for Population with purple color
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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

    fig = fig_to_base64(fig)
    return fig

def incomeAverageexchangerate():
    df = pd.read_excel(file_path)

    average_exchange_rate_column = 'Average exchange rate (yuan/USD)'

    # Create a line plot for Average exchange rate with purple color
    fig=plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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

    fig = fig_to_base64(fig)
    return fig

def incomeEconomicgrowthrate():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Economic growth rate (%)' is the new economic growth rate column name
    economic_growth_rate_column = 'Economic growth rate (%)'

    # Create a line plot for Economic growth rate
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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
    fig = fig_to_base64(fig)
    return fig

def incomeGDP():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Gross domestic product GDP (nominal value, million yuan)' is the GDP column name
    gdp_column = 'Gross domestic product GDP (nominal value, million yuan)'

    # Create a line plot for GDP only
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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
    fig = fig_to_base64(fig)
    return fig

def incomeAverageGDP():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Average GDP per capita (nominal value, yuan)' is the new GDP column name
    gdp_column = 'Average GDP per capita (nominal value, yuan)'

    # Create a line plot for Average GDP per capita
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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
    fig = fig_to_base64(fig)
    return fig

def incomeGNI():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Gross national income GNI (nominal value, million yuan)' is the new GNI column name
    gni_column = 'Gross national income GNI (nominal value, million yuan)'

    # Create a line plot for Gross national income GNI
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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
    fig = fig_to_base64(fig)
    return fig

def incomeAverageGNI():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'Average GNI per person (nominal value, yuan)' is the new GNI per person column name
    gni_per_person_column = 'Average GNI per person (nominal value, yuan)'

    # Create a line plot for Average GNI per person
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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
    fig = fig_to_base64(fig)
    return fig

def incomeNational():
    
    # Load the data into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Assuming 'National income (nominal value, million yuan)' is the new national income column name
    national_income_column = 'National income (nominal value, million yuan)'

    # Reverse the order of the data for the line plot
    reversed_data = df[national_income_column][::-1]

    # Create a line plot for National income
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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
    fig = fig_to_base64(fig)
    return fig

def incomeAverageperson():
    df = pd.read_excel(file_path)

    # Assuming 'Average income per person (nominal value, yuan)' is the new average income per person column name
    average_income_per_person_column = 'Average income per person (nominal value, yuan)'

    # Create a line plot for Average income per person
    fig = plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
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
    fig = fig_to_base64(fig)
    return fig

def kmeansAgeIntention():
    kmeans = os.path.join(script_dir, r'data\房價與結婚意願之相關分析_1214修改版 的副本 (回覆) (1).xlsx')

    # Reading the Excel file with an explicit encoding
    df = pd.read_excel(kmeans)

    # Mapping age ranges to numeric values
    age_mapping = {'21～29': 25, '30～39': 35, '40～49': 45, '50～59': 55, '60以上': 65}
    df['年齡數值'] = df['您的年齡'].map(age_mapping)

    # Mapping salary ranges to numeric values
    salary_mapping = {'0～19999': 10000, '20000～39999': 30000, '40000～59999': 50000, '60000～79999': 70000, '80000以上': 90000}
    df['月薪資數值'] = df['目前月薪資水平(台幣)'].map(salary_mapping)

    # Selecting relevant features for K-means clustering
    features = ['年齡數值', '月薪資數值', '請問買房影響您結婚意願的程度為？']
    data_for_clustering = df[features].dropna()

    # Applying K-means clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    clusters = kmeans.fit_predict(data_for_clustering)

    # Adding cluster information to the dataframe
    data_for_clustering['Cluster'] = clusters

    # Creating a correlation matrix and visualizing it using a heatmap
    correlation_matrix = data_for_clustering.corr()
    fig=plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Heatmap of Correlation Between Age, Monthly Salary, and Influence on Marriage Intention')

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

# import data from .xlxs to database
def importdata():
    # Set up Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analysis.settings")
    django.setup()

    from home.models import MarriageSurvey  
    MarriageSurvey.objects.all().delete()

    # Path to Excel file
    excel_file_path = r"C:\Users\DAIYUNWU\Desktop\Python-data-analysis\analysis\home\data\collect.xlsx"

    # Read the Excel file and insert data into the database
    df = pd.read_excel(excel_file_path)

    for _, row in df.iterrows():
        timestamp_str = str(row["時間戳記"])
        timestamp = timezone.make_aware(pd.Timestamp(timestamp_str).to_pydatetime())

        MarriageSurvey.objects.create(
            timestamp=timestamp,
            gender=row["生理性別"],
            education=row["最高學歷"],
            age=row["您的年齡"],
            salary=row["目前月薪資水平(台幣)"],
            is_married=row["您是否已婚？"],
            marriage_intention = row["您目前是否有結婚意願(不論單身與否)"],
            agree_buying_house = row["您認同買房是影響多數人結婚的重要因素嗎？"],
            buying_house_influence = row["請問買房影響您結婚意願的程度為？"],
            marriage_house_requirement = row["您對結婚一定得買房的認同度為何？"],
            afford_house_price = row["請問您認為自己目前薪資能獨自負擔逐年攀升的房價的程度為？"],
            buying_house_impact_life = row["您認同買房會影響到個人生活水平的程度為？"],
            government_support = row["您認為政府在買房上已擁有完善配套措施的程度為？"],
            family_planning = row["想要與心愛的人共組家庭"],
            desire_for_children = row["想要小孩"],
            legal_recognition = row["想要讓伴侶關係被法律所認同"],
            tradition = row["傳統上結婚是人生的必經之路"],
            responsibility_sharing = row["想要伴侶一同承擔責任"],
            sacrifice_lifestyle = row["不想因為結婚犧牲現有生活水平"],
            affordability = row["無法負擔高額房價"],
            marriage_expenses_affordability = row["無法負擔結婚開銷"],
            stable_career_before_family = row["想要先穩定事業再組建家庭"],
            child_rearing_cost_affordability = row["無法負擔子女教養費用"],
            non_economic_factor_relationship = row["只需要情感需求，不想綁定法律義務"],
            family_adjustment_concerns = row["害怕要與對方家庭磨合"],
            trustworthiness = row["不知是否對方值得信任"],
            fear_of_commitment = row["不想養小孩"],
            freedom_loss_after_marriage = row["婚後會失去自由"],
            no_partner = row["沒有對象"],
            fear_of_marriage_failure = row["害怕婚姻失敗"],
            anycommond = row["任何指教"]
            )