import pandas as pd
from apyori import apriori
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
age = os.path.join(script_dir, "collect.xlsx")
all_columns = pd.read_excel(age, nrows=0).columns.tolist()
df = pd.read_excel(age)
last_column_index = df.index[-1]-1
print("最后一列的索引:", last_column_index)

output_file_path = os.path.join(script_dir, "output.txt")
with open(output_file_path, "w") as output_file:
    for k in range(7,last_column_index):
        for i in range(6):


            selected_columns = [i+1, k]
            selected_columns_names = [all_columns[j] for j in selected_columns]
            
            print(selected_columns_names)
            df = pd.read_excel(age, usecols=selected_columns)
            df = df.astype(str)  # Use this line for replacement

            data_list = df.values.tolist()
            # print(data_list)

            # 使用apriori算法
            results = list(apriori(data_list, min_support=0.1, min_confidence=0.2, min_lift=1.3, max_length=2))

            # print(results)
            # 
            for result in results:
                pair = result[0] 
                products = [x for x in pair]
                output_file.write("Selected Columns: " + str(selected_columns_names) + "\n")
                output_file.write("Rule: " + products[0] + " →" + products[1] + "\n")
                output_file.write("Support: " + str(result[1]) + "\n")
                output_file.write("Confidence: " + str(result[2][0][2]) + "\n")
                if len(result[2]) > 1:
                    output_file.write("Lift: " + str(result[2][1][3]) + "\n")
                else:
                    output_file.write("Lift: N/A\n")
                output_file.write("==================================\n")

print("Output written to:", output_file_path)
