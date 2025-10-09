#
# Sefty, 2025/10/08
# File: Sefty_Excel.py
# Calculate sum of column in Excel file.
#

import pandas as pd

#1. Input
df = pd.read_excel('Financial_Sample.xlsx')

#2. Process
sums = df.select_dtypes(include='number').sum()

#Optionally give a label for the row (e.g., 'Total')
sums['Name'] = 'Total' #Add a value for the non-numeric column

#Append the total row to the DataFrame
df_with_total = pd.concat([df,pd.DataFrame([sums])], ignore_index=True)

#3. Output
print(df_with_total)
df_with_total.to_excel('output.xlsx', index=False)