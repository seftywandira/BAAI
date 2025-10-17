#
# Sefty, 2025/10/15
# File: Sefty_Mini_Project.py
# Short description of the task
# Mini Project: Product Discount Calculator

# (1) Input
# 0. Data Provided:
products = [
{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}
]

# (2) Process
# 1. Initialize tracking variables (declare variables)
total_original = 0
total_discount_amount = 0
total_final = 0

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

#2. Process each product (loop through products)
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    #3. Determine discount based on category and price
    if category=="Electronics":
        if price>=1000:
            discount = 0.2
        elif price>=500:
            discount = 0.15
        else:
            discount = 0.1
        
    elif category=="Clothing":
        if price>=100:
            discount = 0.25
        else:
            discount = 0.15

    elif category=="Books":
        discount = 0.1

    #4. Calculate final price
    final_price = (1-discount)*price

#5. Print product details
    print(f"Product: {name}")
    print(f"  Category: {category}")
    print("  Original Price: %.2f"%price)
    print(f"  Discount: {int(discount*100)}%")
    print("  Final Price: $%.2f\n"%(final_price))

    #6. Update totals
    total_original += price
    total_discount_amount += discount*price
total_final = total_original - total_discount_amount

# (3) Output
#7. Print summary
print("\n=== SUMMARY ===")

#8. Print total statistics
print(f"Total Products: {len(products)}")
print("Total Original Price: $%.2f"%(total_original))
print("Total Discount: $%.2f"%(total_discount_amount))
print("Total Final Price: $%.2f"%(total_final))
