
# Expense manager app

Uma aplicação CLI que permite ao utilizador registar, consultar e eliminar despesas pessoais, armazenando os dados localmente.

## Requirements

- Python 3
- Standard Python library only
- Command-line interface
- Local data persistence
- No external database

## Project Structure

expense-manager/
│
├── src/
│   ├── main.py
│   ├── expenses.py
│   ├── categories.py
│   └── storage.py
│
├── tests/
│   └── ...
│
├── data/
│   └── expenses.csv
│
├── README.md
└── .gitignore

## Functions

- Add expense
- List expenses
- Remove expense
- Filter expenses
  - by category
  - by month
- Show summary
- Exit the app

## Expense

- id;
- date;
- description;
- category;
- amount;

### Categories

- Food
- Transport
- Entertainment
- Housing
- Other

### Operations

- Add
- List
- Remove
- Filter
- Summary
- Exit

### Validation

- Description → non-empty + length limit
- Category    → predefined options
- Amount      → valid monetary value
- Date        → valid date
- ID          → valid existing ID
- Confirmation → y/n
