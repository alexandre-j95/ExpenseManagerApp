
# Start screen

================================
      EXPENSE MANAGER
================================

1. Add expense
2. List expenses
3. Remove expense
4. Filter expenses
5. Show summary
6. Exit

Choose an option:

## 1. Add expense

Choose an option: 1

--- Add Expense ---

Requests a description, category, amount and date

Date (YYYY-MM-DD): 2026-08-08 # Valid date formats
Description: Groceries # Non-empty description withcharacter limit
Category: Food # Predefined list of options
Amount: 42.50 # Valid Monetary amount

Expense added successfully!

Press Enter to return to the menu...

## 2. List expenses

Shows current months expenses

--- Expenses ---

ID   DATE        DESCRIPTION       CATEGORY       AMOUNT
1    2026-08-06  Supermarket       Food           €42.50
2    2026-08-07  Fuel              Transport      €35.00
3    2026-08-08  Cinema            Entertainment  €12.00

Total: €89.50

Press Enter to return to the menu...

## 3. Remove expense

asks for ID of expense to be deleted
shows the expense selected by the ID and asks confirmation
acts upon the choice of the user

--- Remove Expense ---

Enter expense ID: 2

Are you sure you want to remove:

Fuel
Transport
€35.00

(y/n):

### if user enters y

Expense removed successfully

### if user enters n

Operation cancelled.

## 4. Filter expenses

1. By category
2. By month
3. Back

## 5. Show summary

--- Summary ---

August 2026

Total spent: €634.27

By category:

Food           €284.50
Transport      €156.20
Entertainment   €89.99
Housing         €75.00
Other           €28.58

## 6. Exit

Goodbye!

## Invalid menu option

Choose an option: 9

Invalid option. Please choose a number between 1 and 6.

## Invalid amount

Amount: forty euros

Invalid amount. Please enter a valid monetary amount.

Amount:

## Invalid date

Date (YYYY-MM-DD): 2026-99-99

Invalid date. Please use the format YYYY-MM-DD.

Date:

## Invalid expense ID

Enter expense ID: abc

Invalid ID. Please enter a number.

## Non-existent expense

Enter expense ID: 27

No expense found with ID 27.

## Case Study

Input

```
Description: Groceries
Category: Food
Amount: 42.50
Date: 2026-08-08
```

Concept

```
Expense expense = new_expense(description, category, amount, date)
expenses[].join(expense)
with open(expenses.csv, "w") as f:
for expense in expenses:
  f.write(expense)
```

ExpenseClass

- id: Integer
- date: DateType
- description: String
- category: Enum
- amount: Float

Expenses - Array of ExpenseClass

In csv:
id,date,description,category,amount
1,2026-08-08,Groceries,Food,42.50

app starts > populate the array from csv > operate on array > write the array back into csv file 
to populate from csv: split into lines, ignore header, each line is an expense, create the expense objects by taking the comma separated values as arguments.
write back into the csv file using a to string method for each expense object that matches the structure of the csv

----------------

Regarding Ids of the expenses. Since this isn't for a real business and is mostly stored in my personal machine we dont need randomization to mask how many transactions are being made daily.

If there is no expense in the file and no header, we failed to load the correct CSV file.

If there is no expense but header is there, then the first expense will be id = 1.

If there are expenses 1, 2, 3, next expense would be 4

If expense 2 gets "deleted" next expense id would still be 4.

The expense ID comes from an internal counter it won't match up with the index on the array.


## Future Ideas / To Do's 

- Chance the sequential menu inputs using input into having all four fields visible simultaneously and moving an actual cursor up/down between them, with terminal control/keyboard handling (ex: curses).
