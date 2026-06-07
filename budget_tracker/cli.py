from budget_tracker import storage, reports
from budget_tracker.models import Income, Expense, INCOME_CATEGORIES, EXPENSE_CATEGORIES


def _get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Please enter a valid number.")


def _get_choice(prompt: str, options: list) -> str:
    print("  Options:", ", ".join(options))
    while True:
        val = input(prompt).lower().strip()
        if val in options:
            return val
        print(f"  Invalid. Choose from: {', '.join(options)}")


def add_income():
    print("\n--- Add Income ---")
    amount   = _get_float("  Amount: ")
    category = _get_choice("  Category: ", INCOME_CATEGORIES)
    desc     = input("  Description: ").strip()
    t        = Income(amount, category, desc)
    if not t.is_valid():
        print("  Invalid category.")
        return
    storage.save(t)
    print(f"  Saved: {t}")


def add_expense():
    print("\n--- Add Expense ---")
    amount   = _get_float("  Amount: ")
    category = _get_choice("  Category: ", EXPENSE_CATEGORIES)
    desc     = input("  Description: ").strip()
    t        = Expense(amount, category, desc)
    storage.save(t)
    print(f"  Saved: {t}")


def view_summary():
    print("\n--- Summary ---")
    transactions = storage.load()
    if not transactions:
        print("  No transactions yet.")
        return
    data = reports.summary(transactions)
    print(f"  Income  : {data['total_income']:>10.2f}")
    print(f"  Expenses: {data['total_expenses']:>10.2f}")
    print(f"  Balance : {data['balance']:>10.2f}")
    print("\n  By category:")
    for cat, total in sorted(data["by_category"].items()):
        print(f"    {cat:<18} {total:.2f}")


def run():
    print("\n====  Budget Tracker  ====")
    while True:
        print("\n  1. Add income")
        print("  2. Add expense")
        print("  3. View summary")
        print("  4. Export report (CSV)")
        print("  5. Quit")
        choice = input("\n  Choose [1-5]: ").strip()

        if   choice == "1": add_income()
        elif choice == "2": add_expense()
        elif choice == "3": view_summary()
        elif choice == "4":
            reports.export_report(storage.load())
        elif choice == "5":
            print("  Goodbye!")
            break
        else:
            print("  Invalid option. Try 1-5.")