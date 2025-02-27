import datetime

# This is where all the transactions will be stored
transactions = []
balance = 0.0 

# Function to add a transaction (income or expense)
def add_transaction(amount, description, date, transaction_type):
    global balance
    # Create a transaction as a dictionary
    transaction = {
        "amount": amount,
        "description": description,
        "date": date,
        "transaction_type": transaction_type
    }
    transactions.append(transaction)  # Add the transaction to the list
    if transaction_type == "income":
        balance += amount  # Add income to balance
    elif transaction_type == "expense":
        balance -= amount  # Subtract expense from balance

# Function to update a transaction by index
def update_transaction(index, new_amount=None, new_description=None, new_date=None, new_transaction_type=None):
    global balance
    if new_amount:
        transactions[index]["amount"] = new_amount
    if new_description:
        transactions[index]["description"] = new_description
    if new_date:
        transactions[index]["date"] = new_date
    if new_transaction_type:
        transactions[index]["transaction_type"] = new_transaction_type

    # Recalculate balance after update
    balance = 0.0
    for transaction in transactions:
        if transaction["transaction_type"] == "income":
            balance += transaction["amount"]
        elif transaction["transaction_type"] == "expense":
            balance -= transaction["amount"]

# Function to delete a transaction by index
def delete_transaction(index):
    global balance
    transaction = transactions.pop(index)  # Remove the transaction
    if transaction["transaction_type"] == "income":
        balance -= transaction["amount"]
    elif transaction["transaction_type"] == "expense":
        balance += transaction["amount"]

# Function to view current balance
def view_balance():
    return f"Current balance: ${balance:.2f}"

# Function to view all transactions
def view_transactions():
    if not transactions:
        print("No transactions to display.")
    for index, transaction in enumerate(transactions):
        print(f"{index}. {transaction['transaction_type'].capitalize()} | {transaction['description']} | ${transaction['amount']} | {transaction['date']}")

# Function to view summary of income and expenses
def view_summary(start_date=None, end_date=None, description=None):
    income = 0.0
    expense = 0.0
    for transaction in transactions:
        transaction_date = datetime.datetime.strptime(transaction["date"], "%Y-%m-%d")
        if start_date and transaction_date < start_date:
            continue
        if end_date and transaction_date > end_date:
            continue
        if description and transaction["description"].lower() != description.lower():
            continue
        if transaction["transaction_type"] == "income":
            income += transaction["amount"]
        elif transaction["transaction_type"] == "expense":
            expense += transaction["amount"]

    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expense:.2f}")

# Main function with a menu to interact with the user
def main():
    while True:
        print("\n1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View Balance")
        print("5. View Transactions")
        print("6. View Summary")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a transaction its case sensitive so insure your typing it in as you see it in the options
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            transaction_type = input("Enter transaction type (income/expense): ").lower()
            add_transaction(amount, description, date, transaction_type)

        elif choice == "2":
            # Update an existing transaction whether thats updating the date, amount, description or transaction type
            view_transactions()
            index = int(input("Enter transaction index to update: "))
            print("Leave fields blank to not change them.")
            new_amount = input("Enter new amount: ")
            new_amount = float(new_amount) if new_amount else None
            new_description = input("Enter new description: ") or None
            new_date = input("Enter new date (YYYY-MM-DD): ") or None
            new_transaction_type = input("Enter new transaction type (income/expense): ") or None
            update_transaction(index, new_amount, new_description, new_date, new_transaction_type)

        elif choice == "3":
            # Delete a transaction
            view_transactions()
            index = int(input("Enter transaction index to delete: "))
            delete_transaction(index)

        elif choice == "4":
            # Show balance which is calculated by total Income - expenses 
            print(view_balance())

        elif choice == "5":
            # View all transactions, including expenses and income
            view_transactions()

        elif choice == "6":
            # View summary of all income and expenses unless specified otherwise via the filters such as dates and descriptions
            print("Summary of transactions:")
            start_date = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ")
            if start_date:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ")
            if end_date:
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            description = input("Enter description to filter or press Enter to skip: ")
            view_summary(start_date, end_date, description)

        elif choice == "7":
            # Exits out of the tracker
            print("Goodbye 👋!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
