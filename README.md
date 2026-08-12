# Expense Manager App

A small command-line expense tracker written in Python (standard library only).
Track personal expenses, filter them by category or month, and see a running
summary per category. Local CSV storage, no database, no third-party runtime
dependencies.

> Learning project — built while learning backend development. It aims to be
> correct and readable over clever.

## Features

- Add expense (with input validation: date, non-empty description, category,
  monetary amount)
- List all expenses
- Remove expense (with confirmation)
- Filter expenses by category or by month
- Show summary: total spent + breakdown per category
- Data persists to a local CSV file between runs

## Requirements

- Python 3.10+ (uses `match` statements and `X | None` type unions)
- No external packages at runtime

## Installation

```bash
git clone <your-repo-url>
cd ExpenseManagerApp
python3 main.py
```

That's it — there is nothing to install. The app creates
`data/expenses.csv` on first save if it does not already exist.

## Usage

Run the app and pick an option from the menu:

```
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
```

- **Add expense** — enter a date (`YYYY-MM-DD`), description, category (1–5),
  and amount. Invalid input is rejected and re-prompted.
- **List expenses** — prints every stored expense in a table.
- **Remove expense** — enter an ID, confirm with `y`/`n`.
- **Filter expenses** — choose category or month (1–12). Note: month filtering
  currently matches month only, across all years.
- **Show summary** — prints total spent and a per-category breakdown.

## Project structure

```
ExpenseManagerApp/
├── main.py              # CLI menu + user input/output
├── expense_manager.py   # ExpenseManager: in-memory operations on expenses
├── expenses.py          # Expense data class + Category enum + limits
├── storage.py           # load/save CSV, row <-> Expense conversion
├── test_storage.py      # tests for storage load/save
├── test_expenses.py     # tests for the Expense class
├── example.csv          # template CSV (header only)
└── data/
    └── expenses.csv     # your data (created on first save)
```

## Data format

One row per expense, comma-separated, with a header:

```
id,date,description,category,amount
1,2026-08-06,Supermarket,Food,42.50
```

- `id` — integer, assigned sequentially (max existing id + 1), survives restart
- `date` — `YYYY-MM-DD`
- `category` — one of `Food`, `Transport`, `Entertainment`, `Housing`, `Other`
- `amount` — decimal monetary value (stored and summed as `Decimal`, never float)

## Design notes

- **Money is `Decimal`.** Amounts are never `float`, to avoid binary
  floating-point rounding errors in sums and totals.
- **`ExpenseManager` owns the data.** The menu functions in `main.py` do
  input/output only; computation (filter, totals) lives on `ExpenseManager`.
- **Persistence is explicit.** Every add/remove calls `save_expenses(...)` so
  changes are written back to the CSV.
- **Single source of truth.** Expenses are loaded once at startup into an
  in-memory list, operated on, and written back on mutation.

## Testing

Tests use the standard library `unittest` (runnable via `pytest` if installed):

```bash
pytest -v          # if pytest is available
python3 -m unittest discover   # stdlib-only alternative
```

## Roadmap / future ideas

- Scope month filter and summary by year + month (currently month-only)
- A cursor-based menu using terminal control (e.g. `curses`)
- Edit an existing expense
- Export/import and richer reporting

## License

MIT — free to use and learn from.
