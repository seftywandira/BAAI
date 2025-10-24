# Customer Segmentation Tool

# Import necessary libraries
import pandas as pd

# Read the Excel file
file_name = "customers.xlsx"
dataset = pd.read_excel(file_name)

# Since there are trailing and leading spaces around column names and their contents, due to I copy from the instruction. So, I will remove them
dataset.columns = dataset.columns.str.strip()
dataset['Customer_Name'] = dataset['Customer_Name'].str.rstrip()

# Add a "Customer_Category" column and initialize it with empty string
dataset['Customer_Category'] = ""

# Add a "AVG_Order_Value" column and initialize it with zero
dataset['AVG_Order_Value'] = 0

# By masking each row in the data frame, determine segments for each customer based on the money they spent by using boolean data type stored in below variables
is_vip_customer = dataset["Total_Purchases"] > 10000
lower_middle_limit = dataset["Total_Purchases"] >= 5000
is_reg_customer = lower_middle_limit^is_vip_customer
is_new_customer = ~lower_middle_limit

# Create the catagories
dataset.loc[is_vip_customer, "Customer_Category"] = "VIP"
dataset.loc[is_reg_customer, "Customer_Category"] = "Regular"
dataset.loc[is_new_customer, "Customer_Category"] = "New"

# Calculate average order value: 
dataset["AVG_Order_Value"] = round(dataset["Total_Purchases"]/dataset["Number_of_Orders"],2)

# Calculate total VIP revenue
total_vip_revenue = dataset.loc[dataset["Customer_Category"]=="VIP","Total_Purchases"].sum()

# Do segmentation based on the mask
vip_customer = dataset[dataset["Customer_Category"]=="VIP"].reset_index(drop=True)
reg_customer = dataset[dataset["Customer_Category"]=="Regular"].reset_index(drop=True)
new_customer = dataset[dataset["Customer_Category"]=="New"].reset_index(drop=True)

# print(f'is_vip_customer: \n{is_vip_customer}')
# print(f'lower_middle_limit: \n{lower_middle_limit}')
# print(f'is_reg_customer: \n{is_reg_customer}')
# print(f'is_new_customer: \n{is_new_customer}')

# Print out the report
vip_print_bool = False
reg_print_bool = False
new_print_bool = False

print("CUSTOMER SEGMENTATION REPORT")
print("============================")

for i in range(len(vip_customer)):
    if vip_print_bool==False:
        print("VIP Customers:")
        vip_print_bool=True
    print("- {}".format(vip_customer.loc[i, "Customer_Name"])
            +
            " | Total: ${:,}".format(vip_customer.loc [i, "Total_Purchases"])
            +
            " | Orders: {}".format(vip_customer.loc [i, "Number_of_Orders"])
            +
            " | Avg Order: ${:,.2f}".format(vip_customer.loc [i, "AVG_Order_Value"])
    )
print("")
for i in range(len(reg_customer)):
    if reg_print_bool==False:
        print("Regular Customers:")
        reg_print_bool=True
    print("- {}".format(reg_customer.loc[i, "Customer_Name"])
            +
            " | Total: ${:,}".format(reg_customer.loc [i, "Total_Purchases"])
            +
            " | Orders: {}".format(reg_customer.loc [i, "Number_of_Orders"])
            +
            " | Avg Order: ${:,.2f}".format(reg_customer.loc [i, "AVG_Order_Value"])
    )
print("")
for i in range(len(new_customer)):
    if new_print_bool==False:
        print("New Customers:")
        new_print_bool=True
    print("- {}".format(new_customer.loc[i, "Customer_Name"])
            +
            " | Total: ${:,}".format(new_customer.loc [i, "Total_Purchases"])
            +
            " | Orders: {}".format(new_customer.loc [i, "Number_of_Orders"])
            +
            " | Avg Order: ${:,.2f}".format(new_customer.loc [i, "AVG_Order_Value"])
    )
print("")
print("Total VIP Revenue: ${:,}".format(total_vip_revenue))