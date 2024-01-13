import json
import os
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        # Initialize self.expenses with an empty list for each category
        self.expenses = defaultdict(list)

    def input_expense(self):
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the expense category (e.g., food, shopping, transportation, entertainment): ")

        # Make sure the category key exists in the dictionary
        if category not in self.expenses:
            self.expenses[category] = []

        self.expenses[category].append({"amount": amount, "description": description})

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            file.write(json.dumps(self.expenses) + '\n')

    def load_expenses(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                for line in file:
                    data = json.loads(line)
                    for category, entries in data.items():
                        self.expenses[category].extend(entries)

    def monthly_summary(self):
        for category, entries in self.expenses.items():
            total_amount = sum(entry["amount"] for entry in entries)
            print(f"{category.capitalize()}: Rs.{total_amount:.2f}")

    def category_summary(self):
        category = input("Enter the expense category to view its summary: ")
        entries = self.expenses.get(category, [])
        total_amount = sum(entry["amount"] for entry in entries)
        print(f"Total {category.capitalize()} expenses: Rs.{total_amount:.2f}")

def main():
    expense_tracker = ExpenseTracker()
    expense_tracker.load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Input Daily Expense")
        print("2. Monthly Expense Summary")
        print("3. Category-wise Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            expense_tracker.input_expense()
            expense_tracker.save_expenses()
        elif choice == "2":
            expense_tracker.monthly_summary()
        elif choice == "3":
            expense_tracker.category_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
