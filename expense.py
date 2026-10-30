from  datetime import date

class Expense:
    def __init__(self, amount, category, description, expense_date=None):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = expense_date if expense_date is not None else date.today()


    def __str__(self):
        return f"{self.date.isoformat()} | {self.category} | {self.amount:.2f} | {self.description}"

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat(),

        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["amount"],
            data["category"],
            data["description"],
            date.Fromisoformat(data["date"]),
        )
