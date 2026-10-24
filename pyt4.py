
# Multi-Currency Travel Budget Analysis

print("=== TRAVEL BUDGET ANALYSIS ===")

traveler = input("Enter traveler name: ")
budget = float(input("Enter total budget in INR: "))

# Currency details: (currency code, INR conversion rate)
currencies = [
    ("USD", 85.0),
    ("EUR", 95.0),
    ("GBP", 110.0)
]

expenses = []
total_inr = 0

n = int(input("Enter number of expenses: "))

for i in range(n):
    print("\nExpense", i + 1)

    place = input("Enter expense description: ")
    currency = input("Enter currency (INR/USD/EUR/GBP): ").upper()
    amount = float(input("Enter expense amount: "))

    if currency == "INR":
        rate = 1
    else:
        rate = 0

        for item in currencies:
            if item[0] == currency:
                rate = item[1]
                break

    if rate == 0:
        print("Unsupported currency. Expense skipped.")
        continue

    converted = amount * rate
    expenses.append((place, currency, amount, converted))
    total_inr += converted

print("\n========== TRAVEL REPORT ==========")
print("Traveler:", traveler)

for expense in expenses:
    print(expense[0], ":", expense[2], expense[1],
          "= Rs.", round(expense[3], 2))

print("Total Expenses: Rs.", round(total_inr, 2))
print("Travel Budget: Rs.", round(budget, 2))
print("Remaining Budget: Rs.", round(budget - total_inr, 2))

if total_inr <= budget:
    print("Status: Within Budget")
else:
    print("Status: Budget Exceeded")
