
from decimal import Decimal
import datetime
from expenses import (
        Expense,
        Category,
)

class ExpenseManager:

    def __init__(self, expenses: list[Expense], next_id: int) -> None:
        self.expenses = expenses
        self.next_id = next_id

    def add_expense(self, description: str, date: datetime.date, category: Category, amount: Decimal) -> None:
        self.expenses.append( Expense(self.next_id, date, description, category, amount) )
        self.next_id += 1

    def remove(self, expense_id) -> bool:
        for i, expense in enumerate(self.expenses):
            if expense.expense_id == expense_id:
                del self.expenses[i]
                return True
        return False

    def get_by_id(self, expense_id) -> Expense | None:
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        return None

    def get_size(self) -> int:
        return len(self.expenses)

