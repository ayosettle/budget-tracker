import csv
import os
from budget_tracker.models import Income, Expense

DATA_FILE = "data/transactions.csv"
FIELDNAMES = ["type", "amount", "category", "description", "date"]


def _ensure_file():
    """Create the CSV with headers if it doesn't exist."""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def save(transaction):
    """Append a single Transaction to the CSV file."""
    _ensure_file()
    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(transaction.to_dict())


def load() -> list:
    """Load all transactions from CSV, returning a list of objects."""
    _ensure_file()
    transactions = []
    with open(DATA_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row["amount"])
            cls    = Income if row["type"] == "income" else Expense
            transactions.append(
                cls(amount, row["category"], row["description"], row["date"])
            )
    return transactions