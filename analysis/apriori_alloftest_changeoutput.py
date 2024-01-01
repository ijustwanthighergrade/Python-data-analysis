import pandas as pd
from apyori import apriori
import os
import django
import json
# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analysis.settings")
django.setup()

from home.models import MarriageSurvey
from django.db.models import Q
def tuple_to_str(obj):
    if isinstance(obj, tuple):
        return ', '.join(obj)
    return obj
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError
script_dir = os.path.dirname(os.path.abspath(__file__))

# 假設 df 為包含資料的 DataFrame，其中每一列是一位受訪者，每一欄是一個特徵
survey_data = MarriageSurvey.objects.exclude(Q(timestamp__isnull=True) | Q(anycommond__isnull=True)).values()
df = pd.DataFrame(list(survey_data)).drop(columns=['timestamp', 'anycommond'])
for column in df.columns:
    df[column] = df[column].astype(str) + '-' + column
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
for i in range(len(lista)):
    dictforlebal[lista[i]]=listb[i]
# print(dictforlebal)
outputnum=0

# 將 DataFrame 轉換為包含交易的列表
transactions = df.apply(lambda row: frozenset(row.dropna().astype(str)), axis=1).tolist()

# 執行 Apriori 分析
association_rules = apriori(transactions, min_support=0.11, min_confidence=0.6, min_lift=1.3, max_length=6)
association_results = list(association_rules)

jsonfile={}
output_file_path = "apriori_resultstest.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for product in association_results:
        
        pair = product[0] 
        products = list(map(str, [x for x in pair]))
        
        
        # split column name and value
        columnname=[]
        valuename=[]
        for i in range(len(products)):
            # print(products[i])
            value, column = products[i].split('-')
            columnname.append(column)
            valuename.append(value)
        selectedcolumn = [dictforlebal.get(item, item) for item in columnname]
        # change the column name from english to chinese
        data_dict = {}
        # Categorize items with '的' as the main key
        main_key=""
        sub_key=""
        if '：' in selectedcolumn[0]:
            main_key, sub_key = selectedcolumn[0].split('：')
            main_key = main_key.strip()
            sub_key = sub_key.strip()
            print(main_key,sub_key)
        elif '房' in selectedcolumn[0]:
            main_key = '買房觀念'
            sub_key = selectedcolumn[0]
            print(main_key,sub_key)
        else:
            sub_key = selectedcolumn[0]
            main_key = '一般資訊'
            print(main_key,sub_key)
                    
        themostouter_key=main_key
        # print(themostouter_key)
        outer_key= sub_key
        # outer_key= tuple_to_str(tuple(selectedcolumn))
        inner_dict_key=tuple_to_str(tuple(selectedcolumn))
        # print(outer_key,inner_dict_key)
        if themostouter_key not in jsonfile:
            jsonfile[themostouter_key] = {}
        if outer_key not in jsonfile[themostouter_key]:
            jsonfile[themostouter_key][outer_key] = {}
        if inner_dict_key not in jsonfile[themostouter_key][outer_key]:
            jsonfile[themostouter_key][outer_key][inner_dict_key] = []

    
        inner_dict= {
                    "Attibutes": len(selectedcolumn),
                    "Rule": f"{'→ '.join(products)}",
                    "Support": str(product[1]),
                    "Confidence": str(product[2][0][2]),
                }
        if len(product[2]) > 1:
                    inner_dict["Lift"] = str(product[2][1][3])
        else:
            inner_dict["Lift"] = "N\A"
            
        jsonfile[themostouter_key][outer_key][inner_dict_key].append(inner_dict)
        
        # jsonfile={columnname:{valuename[inner_dict]}}
        
        output_file.write(str(outputnum) + "\n")
        output_file.write(f"Columns: {selectedcolumn}\n")
        output_file.write(f"Values: {', '.join(valuename)}\n")
        output_file.write(f"Rule: {'→ '.join(products)}\n")
        output_file.write(f"Support: {str(product[1])}\n")
        output_file.write(f"Confidence: {str(product[2][0][2])}\n")
        outputnum+=1
        # 檢查列表的長度，確保它足夠長
        if len(product[2]) > 1:
            output_file.write(f"Lift: {str(product[2][1][3])}\n")
        else:
            output_file.write("Lift: N/A\n")

        output_file.write("==================================\n")

print(f"Results written to: {output_file_path}")


# 將最終的字典轉換為 JSON 寫入文件
output_json_path = os.path.join(script_dir, "outputtest.json")
with open(output_json_path, "w") as json_file:
    json.dump(jsonfile, json_file, indent=2, default=set_default)

# Print the dictionary
# print("Output Dictionary:")
# print(json.dumps(jsonfile, indent=2, default=set_default))

# print("Output written to:", output_file_path)
# print("Output JSON written to:", output_json_path)
