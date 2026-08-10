import unittest
import datetime
from decimal import Decimal
from expenses import (
    Expense,
    Category,
)

class TestExpense(unittest.TestCase):
    def test_basic_expense(self):

        expense = Expense(1, datetime.date(2026, 8, 8), "test expense", Category.FOOD, Decimal("2.50") )
        result = """Expense_ID: 1
        Expense Date: 2026-08-08
        Expense Description: test expense
        Expense Category: Food
        Expense Amount: 2.50"""

        self.assertEqual(result, f"""Expense_ID: {expense.expense_id}
        Expense Date: {expense.date}
        Expense Description: {expense.description}
        Expense Category: {expense.category.value}
        Expense Amount: {expense.amount}""")




if __name__ == "__main__":
    unittest.main()
