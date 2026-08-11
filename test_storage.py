
import unittest
import tempfile
import os
import datetime
import csv

from decimal import Decimal

from expense_manager import ExpenseManager
from storage import (
    load_expenses,
    save_expenses,
    HEADER,
)

from expenses import (
        Category,
        Expense,
)

class TestLoadExpenses(unittest.TestCase):
    def setUp(self):
        self.path = tempfile.mktemp(suffix='.csv')

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_load_expenses_basic(self):
        with open(self.path, "w") as f:
            f.write(HEADER[0] + "," + ",".join(HEADER[1:]) + "\n")
            f.write("1,2026-08-01,Lunch,Food,5.00\n")
            f.write("2,2026-08-02,Bus,Transport,2.50\n")
        expenses, next_id = load_expenses(self.path)
        self.assertEqual(len(expenses), 2)
        self.assertEqual(next_id, 3)
        self.assertEqual(expenses[0].amount, Decimal("5.00"))
        self.assertEqual(expenses[1].category, Category.TRANSPORT)

    def test_load_expenses_empty(self):
        with open(self.path, 'w') as f:
            f.write(HEADER[0] + "," + ",".join(HEADER[1:]) + "\n")
        expenses, next_id = load_expenses(self.path)
        self.assertEqual(expenses, [])
        self.assertEqual(next_id, 1)


class TestSaveExpenses(unittest.TestCase):
    def setUp(self):
        self.path = tempfile.mktemp(suffix='.csv')

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_save_expenses(self):
        expense0 = Expense(1, datetime.date(2026, 8, 9), "First purchase", Category.OTHER, Decimal("1.01"))
        expense1 =  Expense(2, datetime.date(2026, 8, 9), "Second purchase", Category.FOOD, Decimal("2.02"))
        expenses = [expense0, expense1]
        manager = ExpenseManager(expenses, 3)

        save_expenses(self.path, manager)

        with open(self.path, "r") as f:
            reader = csv.reader(f)
            self.assertEqual(HEADER, next(reader))
            self.assertEqual(["1", "2026-08-09", "First purchase", "Other", "1.01"], next(reader))
            self.assertEqual(["2", "2026-08-09", "Second purchase", "Food", "2.02"], next(reader))





if __name__ == "__main__":
    unittest.main()
