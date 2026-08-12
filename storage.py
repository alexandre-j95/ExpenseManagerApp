import csv
import datetime
from expense_manager import ExpenseManager
from expenses import Expense, Category
from decimal import Decimal

HEADER = ["id", "date", "description", "category", "amount"]


def load_expenses(csv_file: str):
    with open(csv_file, "r", newline="") as f:
        reader = csv.reader(f)
        expenses: list[Expense] = []

        header = next(reader)
        if header != HEADER:
            raise ValueError("invalid header")

        for row in reader:
            expenses.append(row_to_expense(row))

    next_id = 0
    for e in expenses:
        if e.expense_id > next_id:
            next_id = e.expense_id

    return expenses, int(next_id) + 1


def save_expenses(csv_file: str, manager: ExpenseManager) -> None:
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(HEADER)
        for expense in manager.expenses:
            writer.writerow(expense_to_row(expense))


def row_to_expense(row: list[str]) -> Expense:
    expense_id = int(row[0])
    year, month, day = row[1].split("-")
    date = datetime.date(int(year), int(month), int(day))
    description = row[2]
    category = Category(row[3])
    amount = Decimal(row[4])

    expense = Expense(expense_id, date, description, category, amount)
    return expense


def expense_to_row(expense: Expense) -> list[object]:
    return [
        expense.expense_id,
        expense.date,
        expense.description,
        expense.category.value,
        expense.amount,
    ]
