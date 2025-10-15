#
# Sefty, 2025/10/08
# File: Sefty_Excel.py
# Calculate sum of column in Excel file.
#

import pandas as pd

# List of Excel files to preocess
file_list = ['Financial_Sample1.xlsx', 'Financial_Sample2.xlsx'] # Add your files here

for i, file in enumerate(file_list):
    # 1. Input: Read Excel file
    df = pd.read_excel(file)

    # 2. Process: Calculate sum of all numeric columns
    sum_series = df.select_dtypes(include='number').sum()

    # Create a total row DataFrame with the sums
    total_row = pd.DataFrame([sum_series])

    # 3. Append the total row to the original DataFrame
    df_with_total = pd.concat([df,total_row], ignore_index=True)

    # 4. Output: print DataFrame with total row
    print(f'Processed file: {file}')
    print(df_with_total)

    # 5. Save the result into a new Excel File
    output_name = file.replace('.xlsx', '_with_total.xlsx')
    df_with_total.to_excel(output_name, index=False)
    print(f"Saved result to {output_name}")

    # 6. Check if this the last file
    if i == len(file_list)-1:
        print("You reach the last file.")
    else:
        print("Processing next file...\n")

