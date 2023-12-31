import pandas as pd
from apyori import apriori
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
age = os.path.join(script_dir, "collect.xlsx")
all_columns = pd.read_excel(age, nrows=0).columns.tolist()
df = pd.read_excel(age)
# 定義一個將數值轉換為正向、負向或中立的函數
# def classify_value(value):
#     if value >= 4:
#         return '正向'
#     elif value <= 2:
#         return '負向'
#     else:
#         return '中立'
# # 選擇需要進行轉換的欄位
# header_list = df.columns.tolist()
# header_list=['您目前是否有結婚意願(不論單身與否)\n已婚者可以是否後悔結婚來考量', '您認同買房是影響多數人結婚的重要因素嗎？', '請問買房影響您結婚意願的程度為？', 
#              '您對結婚一定得買房的認同度為何？', '請問您認為自己目前薪資能獨自負擔逐年攀升的房價的程度為？', '您認同買房會影響到個人生活水平的程度為？', 
#              '您認為政府在買房上已擁有完善配套措施的程度為？', '可能使擁有結婚意願的因素：想要與心愛的人共組家庭', '可能使擁有結婚意願的因素：想要小孩', 
#              '可能使擁有結婚意願的因素：想要讓伴侶關係被法律所認同', '可能使擁有結婚意願的因素：傳統上結婚是人生的必經之路', 
#              '可能使擁有結婚意願的因素：想要伴侶一同承擔責任', '可能影響您結婚意願的經濟因素：不想因為結婚犧牲現有生活水平', 
#              '可能影響您結婚意願的經濟因素：無法負擔高額房價', '可能影響您結婚意願的經濟因素：無法負擔結婚開銷', 
#              '可能影響您結婚意願的經濟因素：想要先穩定事業再組建家庭', '可能影響您結婚意願的經濟因素：無法負擔子女教養費用', 
#              '可能影響您結婚意願的非經濟因素：只需要情感需求，不想綁定法律義務', '可能影響您結婚意願的非經濟因素：害怕要與對方家庭磨合', 
#              '可能影響您結婚意願的非經濟因素：不知是否對方值得信任', '可能影響您結婚意願的非經濟因素：不想養小孩', 
#              '可能影響您結婚意願的非經濟因素：婚後會失去自由', '可能影響您結婚意願的非經濟因素：沒有對象', '可能影響您結婚意願的非經濟因素：害怕婚姻失敗']
# print(header_list)
# # # 逐一應用函數到每一列
# for column in header_list:
#     df[column] = df[column].apply(classify_value)
# print(df)


# total_columns = len(all_columns)

# last_column_index = df.index[-1]
# print("最后一列的索引:", last_column_index)
# print("最后一欄的索引:", total_columns)
# outputnum=0
# output_file_path = os.path.join(script_dir, "output1.txt")
# with open(output_file_path, "w") as output_file:
#     for k in range(7, total_columns-1):
#         for i in range(k, total_columns-1):
#             if i + 1 < total_columns and k < total_columns:
#                 selected_columns = [i+1, k]
                
#                 selected_columns_names = [all_columns[j] for j in selected_columns]
                
#                 print("Selected Columns:", selected_columns _names)
                
#                 # 複製 DataFrame 以避免改變原始資料
#                 df_copy = df.copy()
                
#                 # 選擇指定列
#                 df_copy = df_copy.iloc[:, selected_columns]
                
#                 # 將資料轉換為字串
#                 df_copy = df_copy.astype(str)
                
#                 print("df_copy:")
#                 print(df_copy)
                
#                 data_list = df_copy.values.tolist()
                
#                 # 使用 apriori
#                 results = list(apriori(data_list, min_support=0.1, min_confidence=0.2, min_lift=1.3, max_length=2))
                
#                 for result in results:
#                     pair = result[0] 
#                     products = [x for x in pair]
#                     outputnum = outputnum + 1
#                     output_file.write(str(outputnum) + "\n")
#                     output_file.write("Selected Columns: " + str(selected_columns_names) + "\n")
#                     output_file.write("Rule: " + products[0] + " →" + products[1] + "\n")
#                     output_file.write("Support: " + str(result[1]) + "\n")
#                     output_file.write("Confidence: " + str(result[2][0][2]) + "\n")
#                     if len(result[2]) > 1:
#                         output_file.write("Lift: " + str(result[2][1][3]) + "\n")
#                     else:
#                         output_file.write("Lift: " + "N\A" + "\n")
#                     output_file.write("==================================\n")

# print("Output written to:", output_file_path)


total_columns = len(all_columns)

last_column_index = df.index[-1]
print("最后一列的索引:", last_column_index)
print("最后一欄的索引:", total_columns)
outputnum=0
output_file_path = os.path.join(script_dir, "output1.txt")
with open(output_file_path, "w") as output_file:
    for k in range(7,total_columns-1):
        for i in range(k,total_columns-1):
            if i + 1 < total_columns and k < total_columns:
                selected_columns = [i+1, k]
                
                selected_columns_names = [all_columns[j] for j in selected_columns]
                
                print(selected_columns_names)
                df = pd.read_excel(age, usecols=selected_columns)
                df = df.astype(str)  # Use this line for replacement

                data_list = df.values.tolist()
                # print(data_list)

                # 使用apriori
                results = list(apriori(data_list, min_support=0.1, min_confidence=0.3, min_lift=1.3, max_length=2))# print(results)
                # 
                
                for result in results:
                    pair = result[0] 
                    products = [x for x in pair]
                    outputnum=outputnum+1
                    output_file.write(str(outputnum)+ "\n")
                    output_file.write("Selected Columns: " + str(selected_columns_names) + "\n")
                    output_file.write("Rule: " + products[0] + " →" + products[1] + "\n")
                    output_file.write("Support: " + str(result[1]) + "\n")
                    output_file.write("Confidence: " + str(result[2][0][2]) + "\n")
                    if len(result[2]) > 1:
                        output_file.write("Lift: " + str(result[2][1][3]) + "\n")
                    else:
                        output_file.write("Lift: " + "N\A" + "\n")
                    output_file.write("==================================\n")

print("Output written to:", output_file_path)
