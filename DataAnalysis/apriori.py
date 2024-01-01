# import pandas as pd
# from apyori import apriori
# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# age = os.path.join(script_dir, "collect.xlsx")
# all_columns = pd.read_excel(age, nrows=0).columns.tolist()
# df = pd.read_excel(age)
# last_column_index = df.index[-1]
# print("最后一列的索引:", last_column_index)
# total_columns = len(all_columns)

# outputnum=0
# output_file_path = os.path.join(script_dir, "output.txt")
# with open(output_file_path, "w") as output_file:
#     for k in range(7,total_columns-1):
#         for i in range(6):

#             selected_columns = [i+1, k]
            
#             selected_columns_names = [all_columns[j] for j in selected_columns]
            
#             print(selected_columns_names)
#             df = pd.read_excel(age, usecols=selected_columns)
#             df = df.astype(str)  # Use this line for replacement

#             data_list = df.values.tolist()
#             # print(data_list)

#             # 使用apriori
#             results = list(apriori(data_list, min_support=0.1, min_confidence=0.3, min_lift=1.3, max_length=3))# print(results)
#             # 
            
#             for result in results:
#                 pair = result[0] 
#                 products = [x for x in pair]
#                 outputnum=outputnum+1
#                 output_file.write(str(outputnum)+ "\n")
#                 output_file.write("Selected Columns: " + str(selected_columns_names) + "\n")
#                 output_file.write("Rule: " + products[0] + " →" + products[1] + "\n")
#                 output_file.write("Support: " + str(result[1]) + "\n")
#                 output_file.write("Confidence: " + str(result[2][0][2]) + "\n")
#                 if len(result[2]) > 1:
#                     output_file.write("Lift: " + str(result[2][1][3]) + "\n")
#                 else:
#                     output_file.write("Lift: " + "N\A" + "\n")
#                 output_file.write("==================================\n")

# print("Output written to:", output_file_path)import pandas as pd
import pandas as pd
from apyori import apriori
import os
import json
outputnum=0
script_dir = os.path.dirname(os.path.abspath(__file__))
age = os.path.join(script_dir, "collect.xlsx")
all_columns = pd.read_excel(age, nrows=0).columns.tolist()
df = pd.read_excel(age)
last_column_index = df.index[-1]
print("最后一列的索引:", last_column_index)
total_columns = len(all_columns)

# ...

output_dict = {}

output_file_path = os.path.join(script_dir, "output.txt")

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for k in range(7, total_columns-1):
        # Move data_list initialization here
        data_list = df.values.tolist()
        for i in range(6):
            selected_columns = [i+1, k]
            selected_columns_names = [all_columns[j] for j in selected_columns]

            print(selected_columns_names)
            if i < len(data_list[0]):  # check if i is within the range

                df_copy = df.copy()
                df_copy = df_copy.iloc[:, selected_columns]
                df_copy = df_copy.astype(str)

                data_list_copy = df_copy.values.tolist()

                # use apriori
                results = list(apriori(data_list_copy, min_support=0.1, min_confidence=0.3, min_lift=1.3, max_length=6))

            for result in results:
                pair = result[0]
                products = [x for x in pair]

                # 構建外層字典的鍵
                outer_key = selected_columns_names[-1]

                # 構建內層字典的鍵 (加入 selected_columns_names)
                inner_dict_key = selected_columns_names[0]

                # 檢查外層字典是否已存在，若不存在則初始化
                if outer_key not in output_dict:
                    output_dict[outer_key] = {}

                # 檢查內層字典是否已存在，若不存在則初始化
                if inner_dict_key not in output_dict[outer_key]:
                    output_dict[outer_key][inner_dict_key] = []

                # 構建內層字典
                inner_dict = {
                    "Rule": f"{products[0]} → {products[1]}",
                    "Support": str(result[1]),
                    "Confidence": str(result[2][0][2]),
                }

                if len(result[2]) > 1:
                    inner_dict["Lift"] = str(result[2][1][3])
                else:
                    inner_dict["Lift"] = "N\A"

                # 將內層字典加入外層字典
                output_dict[outer_key][inner_dict_key].append(inner_dict)

                # 寫入文件
                print("Output for iteration:")
                print("Selected Columns: " + str(selected_columns_names))
                print("Rule: " + inner_dict["Rule"])
                print("Support: " + inner_dict["Support"])
                print("Confidence: " + inner_dict["Confidence"])
                print("Lift: " + inner_dict["Lift"])
                print("==================================")
                outputnum = outputnum + 1
                output_file.write(str(outputnum) + "\n")
                output_file.write("all of selected: " + str(products) + "\n")
                output_file.write("Selected Columns: " + str(selected_columns_names) + "\n")
                output_file.write("Rule: " + inner_dict["Rule"] + "\n")
                output_file.write("Support: " + inner_dict["Support"] + "\n")
                output_file.write("Confidence: " + inner_dict["Confidence"] + "\n")
                output_file.write("Lift: " + inner_dict["Lift"] + "\n")
                output_file.write("==================================\n")
# ...

# 將最終的字典轉換為 JSON 寫入文件
output_json_path = os.path.join(script_dir, "output.json")
with open(output_json_path, "w") as json_file:
    json.dump(output_dict, json_file, indent=2)

# Print the dictionary
print("Output Dictionary:")
print(json.dumps(output_dict, indent=2))

print("Output written to:", output_file_path)
print("Output JSON written to:", output_json_path)
