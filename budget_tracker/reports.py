import csv
from collections import defaultdict
from budget_tracker.models import Income, Expense

def summary(transactions: list) -> dict:
    """Return totals: income, expenses, balance, and per-category breakdown."""
    total_income  = sum(t.amount for t in transactions if isinstance(t, Income))
    total_expense = sum(t.amount for t in transactions if isinstance(t, Expense))

    by_category = defaultdict(float)
    for t in transactions:
        by_category[t.category] += t.amount

    return {
        "total_income":   round(total_income, 2),
        "total_expenses": round(total_expense, 2),
        "balance":        round(total_income - total_expense, 2),
        "by_category":    dict(by_category),
    }


def export_report(transactions: list, filepath: str = "data/report.csv"):
    """Export a summary report grouped by category to a CSV file."""
    data = summary(transactions)
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Total (NGN)"])
        for cat, total in sorted(data["by_category"].items()):
            writer.writerow([cat, f"{total:.2f}"])
        writer.writerow([])
        writer.writerow(["Total Income",   data["total_income"]])
        writer.writerow(["Total Expenses", data["total_expenses"]])
        writer.writerow(["Balance",        data["balance"]])
    print(f"Report exported to {filepath}")