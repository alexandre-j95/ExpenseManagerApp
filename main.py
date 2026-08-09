
from expenses import Expense, Category
import datetime

def main():
    expense = Expense(1, datetime.date(2026, 8, 8), "test expense", Category.FOOD, 2.50)
    print(f"""Expense_ID: {expense.expense_id}
    Expense Date: {expense.date}
    Expense Description: {expense.description}
    Expense Category: {expense.category.value}
    Expense Amount: {expense.amount}""")


main()
