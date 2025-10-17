purchase_amount = 7500

if purchase_amount >= 5000:
    tier = "Platinum"
    discount = 0.20
elif purchase_amount >= 2000:
    tier = "Gold"
    discount = 0.15
elif purchase_amount >= 1000:
    tier = "Silver"
    discount = 0.05

print (f"Customer Tier: {tier}, Discount: {discount*100}%")