
from datetime import datetime
from decimal import Decimal
import os
from expenses import MAX_DESCRIPTION, Category
from storage import load_expenses, save_expenses
from expense_manager import ExpenseManager

PATH_TO_CSV = "data/expenses.csv"

def main():

    version = 0.1
    exiting: bool = False

    expenses, next_id = load_expenses(PATH_TO_CSV)
    manager = ExpenseManager(expenses, next_id)

    while not exiting:

        clear_terminal()
        print(f"Expense Manager App v{version}")

        print("""
================================
      EXPENSE MANAGER
================================

1. Add expense
2. List expenses
3. Remove expense
4. Filter expenses
5. Show summary
6. Exit

Choose an option: """)

        option = input("> ")
        match option:
            case "1":
                select_add_expense(manager)
            case "2":
                select_list_expenses(manager)
            case "3":
                select_remove_expenses(manager)
            case "4":
                select_filter_expenses()
            case "5":
                select_show_summary()
            case "6":
                exiting = select_exit()
            case _:
                print("> Invalid option")
                input("> Press any key to continue...")


def select_add_expense(manager: ExpenseManager):
    print("--- Add Expense ---")

    while True:
        try:
            date = datetime.strptime(input("Date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date. Please use the format YYYY-MM-DD.")
            continue

    while True:
        description = input("Description: ")
        if not description:
            print("> Description cannot be empty...")
            continue
        if len(description) > MAX_DESCRIPTION:
            print(f"> Description cannot exceed {MAX_DESCRIPTION}")
            continue
        break

    while True:
        choices = {1: Category.FOOD, 2: Category.TRANSPORT, 3: Category.ENTERTAINMENT, 4: Category.HOUSING, 5: Category.OTHER}
        print("1) Food  2) Transport  3) Entertainment  4) Housing  5) Other")
        try:
            category = choices[int(input("Category (1-5): "))]
            break
        except ValueError:
            print("Invalid category...")
            continue

    while True:
        value = input("Amount: ")
        try: 
            amount = Decimal(value) 
            break
        except ValueError:
            print("Invalid amount. Please enter a valid monetary amount.")
            continue

    manager.add_expense(description, date, category, amount)
    save_expenses(PATH_TO_CSV, manager)
    print("Expense added successfully!")
    input("Press any key to continue...")

def select_list_expenses(manager: ExpenseManager):
    display_expenses(manager.expenses)
    input("Press any key to continue...")

def select_remove_expenses(manager: ExpenseManager):
    print("--- Remove Expense ---")
    while True:
        expense_id = None
        # get expense id loop
        while True:
            try:
                expense_id = int(input("Enter expense ID: "))
                break
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue
        # get object to delete from list
        to_delete = manager.get_by_id(expense_id)
        if not to_delete:
            print("Expense not found")
            break
        # confirmation loop
        while True:
            print("Are you sure you want to remove:")
            print(to_delete)
            option = input("(y/n): ")
            if option == "y" or option == "n":
                break

        if option == "y":
            manager.remove(to_delete.expense_id)
            save_expenses(PATH_TO_CSV, manager)
            print("Expense removed successfully")
            input("Press any key to continue...")
            break

        print("Operation cancelled.")
        input("Press any key to continue...")
        break


def select_filter_expenses():
    pass

def select_show_summary():
    pass

def select_exit():
    print("Goodbye!")
    return True

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def display_expenses(expenses):
    print(f"{'ID':<3} {'Date':<12} {'Description':<25} {'Category':<18} {'Amount':>10}")
    print("-" * 71)

    for expense in expenses:
        print(
            f"{expense.expense_id:<3} "
            f"{expense.date.strftime('%Y-%m-%d'):<11} "
            f"{expense.description:<24} "
            f"{expense.category.value:<17} "
            f"€{expense.amount:>10.2f}"
        )



if __name__ == "__main__":
    main()
