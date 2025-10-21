# Inventory Reorder System

# Import necessary libraries
import pandas as pd

# Read the Excel file
file_name = "inventory.xlsx"
dataset = pd.read_excel(file_name)

# Since there are trailing and leading spaces around column names and their contents, remove them
dataset.columns = dataset.columns.str.strip()
dataset['Product_Name'] = dataset['Product_Name'].str.rstrip()

# Add a "Reorder_qty" column and initialize it with zero
dataset["Reorder_Qty"] = 0

# Add a "Total_Reorder_Price" column and initialize it with zero
dataset["Total_Reorder_Price"] = 0

# By masking each row in the data frame, determine whether each product quantity is below minimum stock by using boolean data type stored in is_qty_below_min variable
is_qty_below_min = dataset["Current_Stock"] <= dataset["Minimum_Stock"]

# Calculate reorder quantity based on is_qty_below_min variable
dataset.loc[is_qty_below_min, "Reorder_Qty"] = dataset["Minimum_Stock"] - dataset["Current_Stock"] + 10

# Calculate total reorder price for each product
dataset["Total_Reorder_Price"] = dataset["Reorder_Qty"]*dataset["Unit_Price"]

# Calculate total reorder cost
total_reorder_cost = dataset["Total_Reorder_Price"].sum()

print("INVENTORY REORDER REPORT")
print("========================")
print("Products Needing Reorder:\n")

for i in range(len(dataset)):
    if is_qty_below_min[i]:
        print(dataset.loc[i,"Product_Name"]
              +
              ": Reorder "
              +
              str(dataset.loc[i,"Reorder_Qty"])
              +
              " units | Cost: ${:,}".format(dataset.loc[i,"Total_Reorder_Price"])
        )
    else:
        prod_in_good_stock = dataset.loc[i,"Product_Name"]
    
print("\nTotal Reorder Cost: ${:,}".format(total_reorder_cost))
print(f"Product in Good Stock: {prod_in_good_stock}") 