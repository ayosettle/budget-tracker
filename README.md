# 💰 Budget Tracker CLI

A command-line personal finance tool built in Python. Track income and expenses, view category summaries, and export reports to CSV — all from your terminal.

Built as **Project 1** of a structured Junior Python Developer curriculum, covering OOP, File I/O, data structures, error handling, testing, and Git workflow.

---

## Features

- Add income and expense transactions
- Categorise every entry (salary, food, rent, transport, etc.)
- View a live summary: total income, total expenses, and balance
- Breakdown by category
- Export a full report to CSV
- Persistent storage — transactions saved across sessions

---

## Project structure

```
budget-tracker/
├── budget_tracker/
│   ├── __init__.py
│   ├── models.py       # Transaction, Income, Expense classes
│   ├── storage.py      # CSV read/write layer
│   ├── reports.py      # Summary calculations & CSV export
│   └── cli.py          # Interactive menu loop
├── tests/
│   ├── test_models.py
│   ├── test_storage.py
│   └── test_reports.py
├── data/               # Auto-created on first run
│   └── transactions.csv
├── main.py
├── conftest.py
├── pyproject.toml
└── requirements.txt
```

---

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/budget-tracker.git
cd budget-tracker
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python main.py
```

---

## Usage

```
====  Budget Tracker  ====

  1. Add income
  2. Add expense
  3. View summary
  4. Export report (CSV)
  5. Quit
```

### Income categories
`salary` · `freelance` · `investment` · `gift` · `other`

### Expense categories
`food` · `rent` · `transport` · `utilities` · `health` · `entertainment` · `shopping` · `other`

---

## Running the tests

```bash
pytest --cov=budget_tracker --cov-report=term-missing
```

Expected output:

```
collected 9 items

tests/test_models.py   .....   [ 55%]
tests/test_reports.py  ..      [ 77%]
tests/test_storage.py  ..      [100%]

---------- coverage: budget_tracker ----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
budget_tracker/models.py       22      0   100%
budget_tracker/reports.py      18      2    89%
budget_tracker/storage.py      20      1    95%
budget_tracker/cli.py          38     38     0%
-----------------------------------------------
TOTAL                          98     41    58%
```

---

## Roadmap

- [ ] Add date filtering (view transactions by month)
- [ ] Add a `delete` command
- [ ] Colour-coded terminal output with `rich`
- [ ] SQLite backend replacing CSV storage
- [ ] Monthly budget limits with overspend alerts

---

## License

MIT
