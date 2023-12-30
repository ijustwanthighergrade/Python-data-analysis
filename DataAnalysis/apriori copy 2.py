import pandas as pd
from apyori import apriori
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
age = os.path.join(script_dir, "collect.xlsx")

# Get the column names
# Get the column names and create a mapping of column indices to names
all_columns = pd.read_excel(age, nrows=0).columns.tolist()
column_mapping = {i + 1: all_columns[i] for i in range(len(all_columns))}

# Get the total number of columns
total_columns = len(all_columns)

df = pd.read_excel(age)
last_column_index = df.index[-1]
print("最后一列的索引:", last_column_index)

# Create a mapping from column names to indices
column_mapping = {name: idx + 1 for idx, name in enumerate(all_columns)}

outputnum = 0
output_file_path = os.path.join(script_dir, "output2.txt")
with open(output_file_path, "w") as output_file:
    for k in range(7, total_columns - 1):
        for i in range(k, total_columns - 2):
            # Ensure that selected columns are within bounds
            if i + 1 < total_columns and k < total_columns:
                selected_columns = [i + 1, k]

                selected_columns_names = [all_columns[j] for j in selected_columns]

                print(selected_columns_names)
                df_selected = pd.read_excel(age, usecols=selected_columns)
                df_selected = df_selected.astype(str)

                data_list = df_selected.values.tolist()

                # 使用apriori
                # 使用apriori
                results = list(apriori(data_list, min_support=0.1, min_confidence=0.3, min_lift=1.3, max_length=2))

                for result in results:
                    pair = list(result[0])  # Convert frozenset to list

                    # Convert elements in pair to integers
                    pair = [int(item) for item in pair]

                    outputnum += 1
                    output_file.write(str(outputnum) + "\n")
                    output_file.write("Selected Columns: " + str(selected_columns_names) + "\n")

                    # Check if keys exist in the column_mapping dictionary
                    if pair[0] in column_mapping and pair[1] in column_mapping:
                        output_file.write(f"Rule: {column_mapping[pair[0]]} → {column_mapping[pair[1]]}\n")
                        output_file.write(f"Rule: {pair[0]} → {pair[1]}\n")

                    output_file.write("Support: " + str(result[1]) + "\n")
                    output_file.write("Confidence: " + str(result[2][0][2]) + "\n")
                    if len(result[2]) > 1:
                        output_file.write("Lift: " + str(result[2][1][3]) + "\n")
                    else:
                        output_file.write("Lift: " + "N\A" + "\n")
                    output_file.write("==================================\n")
print("Output written to:", output_file_path)
