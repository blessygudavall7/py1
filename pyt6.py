
# ATM Transaction Sequence Simulation

print("=== ATM TRANSACTION SYSTEM ===")

name = input("Enter account holder name: ")
balance = float(input("Enter opening balance: "))

transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful.")
        else:
            print("Enter a valid amount.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
        elif amount <= balance:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif choice == "3":
        print("Account Holder:", name)
        print("Available Balance: Rs.", round(balance, 2))

    elif choice == "4":
        print("\nTransaction History:")

        if len(transactions) == 0:
            print("No transactions available.")
        else:
            for transaction in transactions:
                print(transaction[0], "- Rs.", transaction[1])

    elif choice == "5":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Try again.")
