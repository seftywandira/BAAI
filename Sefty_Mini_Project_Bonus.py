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

#Bonus 1-1-1 (Define variable for highest discount amount)
highest_discount_amount = 0
#Bonus 1-1-4 (Define variable for product with highest discount amount)
product_highest_discount = ""
#Bonus 1-2-1 (Define variable for Calculate the average discount percentage)
discount_sum = 0
#Bonus 2-1-1 (Count how many products are in each category)
electronic_products = 0
clothing_products = 0
book_products = 0
#Bonus 2-2-1
expensive_final_price = 0
expensive_product = ""
cheapest_final_price = 99999999
cheapest_product = ""
#Bonus 3-1-1
total_voucher_given = 0

#2. Process each product (Loop through products)
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]
    
    if category=="Electronics": #== : use fsdfsdfsfew
        #3. Determine discount based on category and price
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
        #Bonus 2-1-2 Electronics Products
        electronic_products += 1

    elif category=="Clothing":
        if price>=100:
            discount = 0.25
            # total_original += price
            # total_discount_amount += discount*price
        else:
            discount = 0.15
            # total_original += price
            # total_discount_amount += discount*price
        #Bonus 2-1-3 Clothing Products
        clothing_products += 1

    elif category=="Books":
        discount = 0.1
        # total_original += price
        # total_discount_amount += discount*price
        #Bonus 2-1-4 Book Products
        book_products += 1

    #4. Calculate final price
    final_price = (1-discount)*price

    #Bonus 2-2-2 (Find the highest discount)
    if final_price > expensive_final_price:
        expensive_final_price = final_price
        expensive_product = name

    if final_price < cheapest_final_price:
        cheapest_final_price = final_price
        cheapest_product = name    

    #Bonus 1-1-2 (Find the highest discount)
    if discount*price > highest_discount_amount:
        highest_discount_amount = discount*price
        #Bonus 1-1-5 (Find the product with highest discount)
        product_highest_discount = name
    #Bonus 3-1-2
    if discount >= 0.2:
        total_voucher_given += 1


#5. Print product details
    print(f"Product: {name}")
    print(f"  Category: {category}")
    print("  Original Price: %.2f"%price)
    print(f"  Discount: {int(discount*100)}%")
    print("  Final Price: $%.2f\n"%(final_price))

    #6. Update totals
    total_original += price
    total_discount_amount += discount*price
    #Bonus 1-2-2 (sum the discount given)
    discount_sum += discount
total_final = total_original - total_discount_amount
avg_discount = discount_sum/len(products)   

#7. Print summary
print("\n=== SUMMARY ===")

#8. Print total statistics
print(f"Total Products: {len(products)}")
print("Total Original Price $%.2f"%(total_original))
print("Total Discount: $%.2f"%(total_discount_amount))
print("Total Final Price: $%.2f"%(total_final))

#Bonus 1-1-3 (display the highest discount amount)
print("Highest Discount Amount: $%.2f"%(highest_discount_amount))
#Bonus 1-1-6 (display the product with the highest discount amount)
print("Product with Highest Discount Amount: %s"%(product_highest_discount))
#Bonus 1-2-3 (display the average discount percentage across all products)
print("AVG Disc %s across all products: %.2f%s"%('%',avg_discount*100,'%'))
#Bonus 2-1-5 (display how many products are in each category)
print("Electronic Products: %i"%(electronic_products))
print("Clothing Products: %i"%(clothing_products))
print("Book Products: %i"%(book_products))
#Bonus 2-2-3 (display the most expensive and cheapest product after discount)
print("Expensive Product after Discount: %s"%(expensive_product))
print("Cheapest Product after Discount: %s"%(cheapest_product))
#Bonus 3-1-3 (display special “Clearance” tag for products with discount >= 20%)
print("You bought %i item(s) with disc. >=20%s. You Get %i voucher(s)."%(total_voucher_given,"%",total_voucher_given))
#Bonus 3-2-1 (display calculate total savings for the customer)
print("Total Savings: %.2f"%total_discount_amount)