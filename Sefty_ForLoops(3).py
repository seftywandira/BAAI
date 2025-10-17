order_values = [120, 450, 80, 300, 650]
total_revenue = 0

for order in order_values:
    total_revenue += order
    print (f"Processing order: ${order}")

print (f"\nTotal Revenue: ${total_revenue}")


