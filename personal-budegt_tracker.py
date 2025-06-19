import json

FILENAME = "budgets.json"

budgets = []

#function to add income()
def add_income():
    description = input("Enter income description: ")
    try:
        amount = float(input("Enter amount: "))
        budgets.append({
            "type": "income",
            "description": description,
            "amount": amount
        })
        print("Income added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    print("\nAll Transactions: ")
    for transaction in budgets:
        sign = "+" if transaction["type"] == "income" else "-"
        print(f"[{transaction['type'].capitalize()}] {transaction['description']}")

#Function to calculate and show balance
def view_balance():
    income = sum(txn["amount"] for txn in budgets if txn["type"] == "income")
    expense = sum(txn["amount"] for txn in budgets if txn["type"] == "expense")
    balance = income - expense
    print(f"\nTotal Balance: #{balance:,.2f}")

# Main Menu loop
while True:
    print("\n==== Personal Budget Tracker ====")
    print("1. Add Income")
    print("2. View transactions")
    print("3. View balance")
    print("4.Exit")

    choice = input("choose an option: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        view_balance()
    elif choice == "4":
        print("Goodby!!!e")
        break
    else:
        print("Invlaid choice. Please select 1,2,3, or 4")

