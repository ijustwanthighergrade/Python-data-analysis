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

# 假設 df 為包含你的資料的 DataFrame，其中每一列是一位受訪者，每一欄是一個特徵
# 這邊使用部分資料作為範例
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

#  dictforlebal={'gender': '生理性別', 'education': '最高學歷', 'age': '您的年齡', 'salary': '目前月薪資水平(台幣)', 'is_married': '您是否已婚？', 'marriage_intention': '您目前是否有結婚意願(不論單身與否)'
#               , 'agree_buying_house': '您認同買房是影響多數人結婚的重要因素嗎？', 'buying_house_influence': '請問買房影響您結婚意願的程度為？', 'marriage_house_requirement': '您對結婚一定得買房的認同度為何？'
#               , 'afford_house_price': '請問您認為自己目前薪資能獨自負擔逐年攀升的房價的程度為？', 'buying_house_impact_life': '您認同買房會影響到個人生活水平的程度為？'
#               , 'government_support': '您認為政府在買房上已擁有完善配套措施的程度為？', 'family_planning': '想要與心愛的人共組家庭', 'desire_for_children': '想要小孩', 
#               'legal_recognition': '想要讓伴侶關係被法律所認同', 'tradition': '傳統上結婚是人生的必經之路', 
#               'responsibility_sharing': '想要伴侶一同承擔責任', 'sacrifice_lifestyle': '不想因為結婚犧牲現有生活水平',
#               'affordability': '無法負擔高額房價', 'marriage_expenses_affordability': '無法負擔結婚開銷', 
#               'stable_career_before_family': '想要先穩定事業再組建家庭', 
#               'child_rearing_cost_affordability': '無法負擔子女教養費用', 
#               'non_economic_factor_relationship': '只需要情感需求，不想綁定法律義務', 
#               'family_adjustment_concerns': '害怕要與對方家庭磨合',      
# 'trustworthiness': '不知是否對方值得信任', 'fear_of_commitment': '不想養小孩', 
# 'freedom_loss_after_marriage': '婚後會失去自由', 'no_partner': '沒有對象', 'fear_of_marriage_failure': '害怕婚姻失敗'}
dictforlebal={}
for i in range(len(lista)):
    dictforlebal[lista[i]]=listb[i]
# 確認 DataFrame 中包含的欄位
# print(dictforlebal)
outputnum=0

# 將 DataFrame 轉換為包含交易的列表
transactions = df.apply(lambda row: frozenset(row.dropna().astype(str)), axis=1).tolist()

# 執行 Apriori 分析
association_rules = apriori(transactions, min_support=0.12, min_confidence=0.6, min_lift=1.3, max_length=20)
association_results = list(association_rules)

jsonfile={}
output_file_path = "apriori_results.txt"
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
        
        themostouter_key=len(selectedcolumn)
        
        outer_key= selectedcolumn[0]
        # outer_key= tuple_to_str(tuple(selectedcolumn))
        inner_dict_key=tuple_to_str(tuple(selectedcolumn))
        print(outer_key,inner_dict_key)
        if themostouter_key not in jsonfile:
            jsonfile[themostouter_key] = {}
        if outer_key not in jsonfile[themostouter_key]:
            jsonfile[themostouter_key][outer_key] = {}
        if inner_dict_key not in jsonfile[themostouter_key][outer_key]:
            jsonfile[themostouter_key][outer_key][inner_dict_key] = []

    
        inner_dict= {
                    # "Values": f"{', '.join(selectedcolumn)}",
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
output_json_path = os.path.join(script_dir, "output.json")
with open(output_json_path, "w") as json_file:
    json.dump(jsonfile, json_file, indent=2, default=set_default)

# Print the dictionary
print("Output Dictionary:")
print(json.dumps(jsonfile, indent=2, default=set_default))

print("Output written to:", output_file_path)
print("Output JSON written to:", output_json_path)
