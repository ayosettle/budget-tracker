from budget_tracker.models import Income, Expense
from budget_tracker.reports import summary

def make_transactions():
    return [
        Income(3000, "salary", "Base pay"),
        Expense(800,  "rent",  "Monthly rent"),
        Expense(200,  "food",  "Groceries"),
    ]

def test_summary_totals():
    data = summary(make_transactions())
    assert data["total_income"]   == 3000.0
    assert data["total_expenses"] == 1000.0
    assert data["balance"]        == 2000.0

def test_summary_by_category():
    data = summary(make_transactions())
    assert data["by_category"]["rent"] == 800.0
    assert data["by_category"]["food"] == 200.0