# Create a program that:
# 1. Processes a list of products
# 2. Applies appropriate discounts based on rules
# 3. Calculates final prices
# 4. Displays a summary report

#Data Provided:
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

# Discount Rules:
# • Electronics:
# – If price >= $1000: 20% discount
# – If price >= $500: 15% discount
# – Otherwise: 10% discount
# • Clothing:
# – If price >= $100: 25% discount
# – Otherwise: 15% discount
# • Books:
# – 10% discount (flat rate)

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

#1. Initialize tracking variables (Declare variables)
total_original = 0
total_discount_amount = 0
total_final = 0

#2. Process each product (Loop through products)
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]
    
    if category=="Electronics":
        if price>=1000:
            discount = 0.2
            # total_original += price #=- : sdfdfdfw
            # total_discount_amount += discount*price
        elif price>=500:
            discount = 0.15
            # total_original += price
            # total_discount_amount += discount*price
        else:
            discount = 0.1
            # total_original += price
            # total_discount_amount += discount*price
        
    elif category=="Clothing":
        if price>=100:
            discount = 0.25
            # total_original += price
            # total_discount_amount += discount*price
        else:
            discount = 0.15
            # total_original += price
            # total_discount_amount += discount*price

    elif category=="Books":
        discount = 0.1
        # total_original += price
        # total_discount_amount += discount*price

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

#7. Print summary
print("\n=== SUMMARY ===")

#8. Print total statistics
print(f"Total Products: {len(products)}")
print("Total Original Price: $%.2f"%(total_original))
print("Total Discount: $%.2f"%(total_discount_amount))
print("Total Final Price: $%.2f"%(total_final))
