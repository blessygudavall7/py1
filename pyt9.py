
# Multi-Product Shopping Budget Constraint

print("=== SMART SHOPPING BUDGET SYSTEM ===")

customer = input("Enter customer name: ")
budget = float(input("Enter your shopping budget: "))

products = []
total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity. Product skipped.")
        continue

    cost = price * quantity

    # Add product only if it fits the budget
    if total + cost <= budget:
        products.append((name, price, quantity, cost))
        total += cost
        print("Product added to shopping list.")
    else:
        print("Product skipped: Budget limit exceeded.")

print("\n========== SHOPPING SUMMARY ==========")
print("Customer:", customer)

for product in products:
    print(product[0], "- Quantity:", product[2],
          "- Cost: Rs.", product[3])

print("Budget: Rs.", round(budget, 2))
print("Total Cost: Rs.", round(total, 2))
print("Remaining Budget: Rs.", round(budget - total, 2))
print("Products Purchased:", len(products))
print("======================================")
