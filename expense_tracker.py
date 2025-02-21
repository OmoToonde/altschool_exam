import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title: str, amount: float):
        """Initialize an Expense object with title, amount, and timestamps."""
        self.id = str(uuid.uuid4())  
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)  
        self.updated_at = self.created_at  

    def update(self, title=None, amount=None):
        """Update title or amount, and refresh the updated_at timestamp."""
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)  

    def to_dict(self):
        """Return a dictionary representation of the expense."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


class ExpenseDatabase:
    def __init__(self):
        """Initialize an empty list to store Expense objects."""
        self.expenses = []

    def add_expense(self, expense: Expense):
        """Add an Expense object to the database."""
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        """Remove an expense by ID."""
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        """Retrieve an expense by its ID."""
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if not found

    def get_expense_by_title(self, expense_title: str):
        """Retrieve a list of expenses matching a given title."""
        return [exp for exp in self.expenses if exp.title.lower() == expense_title.lower()]

    def to_dict(self):
        """Return a list of dictionaries representing all expenses."""
        return [expense.to_dict() for expense in self.expenses]


# Example usage:
if __name__ == "__main__":
    # Create an Expense object
    expense1 = Expense(title="Groceries", amount=50.25)
    expense2 = Expense(title="Transport", amount=15.75)

    # Create an ExpenseDatabase
    db = ExpenseDatabase()

    # Add expenses
    db.add_expense(expense1)
    db.add_expense(expense2)

    # Print all expenses in dictionary format
    print(db.to_dict())

    # Update an expense
    expense1.update(amount=60.00)

    # Retrieve and print an expense by ID
    retrieved_expense = db.get_expense_by_id(expense1.id)
    print(retrieved_expense.to_dict() if retrieved_expense else "Expense not found")

    # Remove an expense
    db.remove_expense(expense2.id)

    # Print the updated expense list
    print(db.to_dict())
