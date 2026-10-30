import json
from expense import Expense
def save_expenses(expenses, filename="expenses.json"):
    data = [e.to_dice() for e in expenses]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    return [Expense.from_dict(d) for d in data]

if __name__ == "__main__":
    items = [
        Expense(450, "Food", "Lunch"),
        Expense(1200.5, "Transport", "Bus pass"),
    ]
    save_expenses(items)
    loaded = load_expenses()
    for e in loaded:
        print(e)