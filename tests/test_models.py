# tests/test_models.py
import pytest
from budget_tracker.models import Income, Expense

def test_income_created_correctly():
    t = Income(500.0, "salary", "Monthly pay")
    assert t.amount == 500.0
    assert t.category == "salary"

def test_amount_rounded_to_two_decimals():
    t = Expense(19.999, "food", "Lunch")
    assert t.amount == 20.0

def test_negative_amount_raises():
    with pytest.raises(ValueError):
        Income(-100, "salary", "test")

def test_income_valid_category():
    assert Income(100, "salary", "pay").is_valid() is True

def test_income_invalid_category():
    assert Income(100, "pizza", "lunch").is_valid() is False