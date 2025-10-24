# Sales Performance Analyzer

# Import necessary libraries
import pandas as pd

# Read the Excel file
file_name = "sales_data.xlsx" 
dataset = pd.read_excel(file_name)

# Since there are trailing and leading spaces around column names and their contents,
# due to I copy from the instruction. So, I will remove them
dataset.columns = dataset.columns.str.strip()
dataset['Employee_Name'] = dataset['Employee_Name'].str.rstrip()

# Add a "Target_Status" column and initialize it with empty string
dataset['Target_Status'] = ""

# Add a "Bonus_Amount" column and initialize it with zero
dataset['Bonus_Amount'] = 0

# By masking each row in the data frame, determine whether each employee met their sales target by using boolean data type stored in is_target_met variable
is_target_met = dataset["Monthly_Sales"] >= dataset["Sales_Target"]

# Label each employee's target_status based on is_target_met variable
dataset.loc[is_target_met, "Target_Status"] = "Target MET"
dataset.loc[~is_target_met, "Target_Status"] = "Target NOT MET"

# Calculate bonus: 10% of sales if target met, 5% if not met 
# Calculate each employee's Bonus_Amount based on is_target_met variable
dataset.loc[is_target_met, "Bonus_Amount"] = 0.1*dataset["Monthly_Sales"]
dataset.loc[~is_target_met, "Bonus_Amount"] = 0.05*dataset["Monthly_Sales"]

# Calculate total bonus to pay
total_bonus = dataset["Bonus_Amount"].sum()
print(f"is_target_met: \n{is_target_met}")
# print("SALES PERFORMANCE REPORT")
# print("========================")
# for i in range(len(dataset)):
#     print(dataset.loc[i,"Employee_Name"]
#           +
#           ": "+dataset.loc[i,"Target_Status"]
#           +
#           " | Sales: ${:,}".format(dataset.loc[i,"Monthly_Sales"])
#           +
#           " | Bonus: ${:,}".format(dataset.loc[i,"Bonus_Amount"])
#     )

# # Calculate and print Total Bonus Amount
# print("\nTotal Bonuses to Pay: ${:,}".format(total_bonus))