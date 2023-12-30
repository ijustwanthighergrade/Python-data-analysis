import pandas as pd
from apyori import apriori
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
age = os.path.join(script_dir, "collect.xlsx")
all_columns = pd.read_excel(age, nrows=0).columns.tolist()
df = pd.read_excel(age)

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
