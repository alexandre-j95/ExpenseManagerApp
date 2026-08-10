
from enum import Enum
from decimal import Decimal
import datetime

MAX_DESCRIPTION: int = 100

class Category(Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    ENTERTAINMENT = "Entertainment"
    HOUSING = "Housing"
    OTHER = "Other"

class Expense:
    """Represents a single personal expense."""
    def __init__(self, expense_id: int, date: datetime.date, description: str, category: Category, amount: Decimal) -> None:
        self.expense_id = expense_id
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount


def add_expense(expenses: list[Expense],
                date: datetime.date,
                description: str,
                category: Category,
                amount: Decimal,
                next_id: int):
    expense = Expense(next_id, date, description, category, amount)
    expenses.append(expense)
    next_id += 1
    return next_id;
