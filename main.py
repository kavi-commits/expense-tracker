from datetime import datetime

from expense import Expense
from storage import load_expenses, save_expenses
from validators import get_int_in_range, get_positive_number


def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Delete expense")
    print("4. Total spending")
    print("5. Summary by category")
    print("6. Filter by month")
    print("7. Quit")


def add_expense(expenses):
    amount = get_positive_number("Amount: ")

    category = input("Category: ").strip().title()
    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip().title()

    description = input("Description: ").strip()

    expenses.append(Expense(amount, category, description))
    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(i, e)


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return
    view_expenses(expenses)
    number = get_int_in_range("Number to delete (0 to cancel): ", 0, len(expenses))
    if number == 0:
        print("Cancelled.")
        return
    removed = expenses.pop(number - 1)
    save_expenses(expenses)
    print(f"Deleted: {removed}")


def total_spending(expenses):
    total = sum(e.amount for e in expenses)
    print(f"Total spending: {total:.2f}")


def summary_by_category(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e.category] = totals.get(e.category, 0) + e.amount
    for category, amount in sorted(totals.items()):
        print(f"{category}: {amount:.2f}")
    print(f"Total: {sum(totals.values()):.2f}")


def filter_by_month(expenses):
    while True:
        text = input("Month (YYYY-MM, blank to cancel): ").strip()
        if not text:
            print("Cancelled.")
            return
        try:
            month = datetime.strptime(text, "%Y-%m")
        except ValueError:
            print("Invalid month. Use YYYY-MM, e.g. 2026-10.")
            continue
        break

    matches = [
        e for e in expenses
        if e.date.year == month.year and e.date.month == month.month
    ]
    if not matches:
        print(f"No expenses in {text}.")
        return
    for e in matches:
        print(e)
    print(f"Total for {text}: {sum(e.amount for e in matches):.2f}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = get_int_in_range("Choose 1-7: ", 1, 7)

        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            delete_expense(expenses)
        elif choice == 4:
            total_spending(expenses)
        elif choice == 5:
            summary_by_category(expenses)
        elif choice == 6:
            filter_by_month(expenses)
        elif choice == 7:
            print("Goodbye.")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")