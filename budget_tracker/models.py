from datetime import date

INCOME_CATEGORIES  = ["salary", "freelance", "investment", "gift", "other"]
EXPENSE_CATEGORIES = ["food", "rent", "transport", "utilities", "health",
                       "entertainment", "shopping", "other"]

class Transaction:
    """Base class for all financial transactions."""

    def __init__(self, amount: float, category: str,
                 description: str, date_str: str = None):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.amount      = round(amount, 2)
        self.category    = category.lower().strip()
        self.description = description.strip()
        self.date        = date_str or str(date.today())

    def to_dict(self) -> dict:
        return {
            "type":        self.__class__.__name__.lower(),
            "amount":      self.amount,
            "category":    self.category,
            "description": self.description,
            "date":        self.date,
        }

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"amount={self.amount}, category='{self.category}', "
                f"date='{self.date}')")


class Income(Transaction):
    def is_valid(self) -> bool:
        return self.category in INCOME_CATEGORIES


class Expense(Transaction):
    def is_valid(self) -> bool:
        return self.category in EXPENSE_CATEGORIES