import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store expenses
EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()
    if description and amount:
        try:
            amount = float(amount)
            expenses.append({"description": description, "amount": amount})
            save_expenses(expenses)
            description_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            update_expense_list()
            update_total_expenses()
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")
    else:
        messagebox.showerror("Input Error", "Please enter both description and amount.")

def update_expense_list():
    expense_list.delete(0, tk.END)
    for expense in expenses:
        expense_list.insert(tk.END, f"{expense['description']}: ${expense['amount']:.2f}")

def update_total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    total_expenses_label.config(text=f"Total Expenses: ${total:.2f}")

def delete_expense():
    selected = expense_list.curselection()
    if selected:
        expenses.pop(selected[0])
        save_expenses(expenses)
        update_expense_list()
        update_total_expenses()
    else:
        messagebox.showwarning("Selection Error", "Please select an expense to delete.")

# Initialize expenses
expenses = load_expenses()

# Sample expenses for testing
if not expenses:
    sample_expenses = [
        {"description": "Coffee", "amount": 3.50},
        {"description": "Groceries", "amount": 45.20},
        {"description": "Transport", "amount": 12.00}
    ]
    expenses.extend(sample_expenses)
    save_expenses(expenses)

# Create the main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Create and place UI elements
description_label = tk.Label(root, text="Description:")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()

expense_list = tk.Listbox(root, width=50)
expense_list.pack()

delete_button = tk.Button(root, text="Delete Selected Expense", command=delete_expense)
delete_button.pack()

# Label to display total expenses
total_expenses_label = tk.Label(root, text="Total Expenses: $0.00")
total_expenses_label.pack()

# Initial update of the expense list and total
update_expense_list()  # Populate the listbox with existing expenses
update_total_expenses()  # Display total expenses

# Run the application
root.mainloop()
