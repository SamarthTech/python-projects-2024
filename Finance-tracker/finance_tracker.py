import csv
from datetime import datetime

class FinanceTracker:
    def __init__(self, filename):
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                self.transactions = list(reader)
        except FileNotFoundError:
            self.transactions = []

    def save_transactions(self):
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transactions)

    def add_transaction(self, category, amount, description):
        date = datetime.now().strftime("%Y-%m-%d")
        transaction = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        self.transactions.append(transaction)
        self.save_transactions()

    def view_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction['date']} | {transaction['category']} | ${transaction['amount']} | {transaction['description']}")

    def get_balance(self):
        return sum(float(t['amount']) for t in self.transactions)

def main():
    tracker = FinanceTracker('transactions.csv')

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category = input("Enter category: ")
            amount = input("Enter amount (use negative for expenses): ")
            description = input("Enter description: ")
            tracker.add_transaction(category, amount, description)
            print("Transaction added successfully!")

        elif choice == '2':
            tracker.view_transactions()

        elif choice == '3':
            balance = tracker.get_balance()
            print(f"Current Balance: ${balance:.2f}")

        elif choice == '4':
            print("Thank you for using the Personal Finance Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()