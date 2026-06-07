import os, pytest
from budget_tracker import storage
from budget_tracker.models import Income, Expense

@pytest.fixture(autouse=True)
def clean_data(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "test.csv"))

def test_save_and_load_roundtrip():
    t = Expense(75.50, "food", "Groceries")
    storage.save(t)
    loaded = storage.load()
    assert len(loaded) == 1
    assert loaded[0].amount == 75.50
    assert loaded[0].category == "food"

def test_load_returns_correct_types():
    storage.save(Income(1000, "salary", "Work"))
    storage.save(Expense(200, "rent", "Monthly rent"))
    loaded = storage.load()
    assert isinstance(loaded[0], Income)
    assert isinstance(loaded[1], Expense)