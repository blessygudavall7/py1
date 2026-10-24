
# Retail Billing with Multiple Discount Rules

print("=== RETAIL BILLING SYSTEM ===")

customer = input("Enter customer name: ")
membership = input("Are you a member? (yes/no): ").lower()

items = []
total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    product = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    items.append((product, price, quantity, amount))
    total += amount

# Discount rules
if total >= 5000:
    discount_rate = 0.15
elif total >= 2000:
    discount_rate = 0.10
elif total >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = total * discount_rate

# Additional membership discount
if membership == "yes":
    membership_discount = (total - discount) * 0.05
else:
    membership_discount = 0

final_bill = total - discount - membership_discount

print("\n========== FINAL BILL ==========")
print("Customer:", customer)

for item in items:
    print(item[0], "- Rs.", item[3])

print("Total Amount: Rs.", round(total, 2))
print("Purchase Discount: Rs.", round(discount, 2))
print("Membership Discount: Rs.", round(membership_discount, 2))
print("Final Amount: Rs.", round(final_bill, 2))
print("================================")
