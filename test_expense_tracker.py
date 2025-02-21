import unittest
from expense_tracker import Expense, ExpenseDatabase  
from datetime import datetime, timezone
import uuid


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        """Runs before each test. Initializes the ExpenseDatabase."""
        self.db = ExpenseDatabase()

    def test_add_multiple_expenses_with_same_title(self):
        """Test that get_expense_by_title() retrieves multiple expenses correctly."""
        expense1 = Expense(title="Coffee", amount=5.00)
        expense2 = Expense(title="Coffee", amount=3.50)
        expense3 = Expense(title="Lunch", amount=12.99)

        self.db.add_expense(expense1)
        self.db.add_expense(expense2)
        self.db.add_expense(expense3)

        coffee_expenses = self.db.get_expense_by_title("Coffee")
        self.assertEqual(len(coffee_expenses), 2)  
        self.assertEqual(coffee_expenses[0].title, "Coffee")
        self.assertEqual(coffee_expenses[1].title, "Coffee")

    def test_remove_non_existent_expense(self):
        """Test that removing a non-existent expense doesn't break the program."""
        initial_count = len(self.db.expenses)
        fake_expense_id = str(uuid.uuid4())  
        self.db.remove_expense(fake_expense_id)
        self.assertEqual(len(self.db.expenses), initial_count)  

    def test_update_only_title(self):
        """Test that updating only the title changes updated_at but keeps the amount."""
        expense = Expense(title="Dinner", amount=20.00)
        self.db.add_expense(expense)
        
        old_updated_at = expense.updated_at  
        expense.update(title="Evening Dinner")  
        
        self.assertEqual(expense.title, "Evening Dinner")  
        self.assertEqual(expense.amount, 20.00)  
        self.assertNotEqual(expense.updated_at, old_updated_at)  
    def test_get_expense_by_id(self):
        """Test retrieving an expense by ID."""
        expense = Expense(title="Gym", amount=30.00)
        self.db.add_expense(expense)

        retrieved_expense = self.db.get_expense_by_id(expense.id)
        self.assertIsNotNone(retrieved_expense)  
        self.assertEqual(retrieved_expense.title, "Gym")

    def test_to_dict_output(self):
        """Test that to_dict() method returns the expected dictionary format."""
        expense = Expense(title="Rent", amount=500.00)
        expense_dict = expense.to_dict()

        self.assertEqual(expense_dict["title"], "Rent")
        self.assertEqual(expense_dict["amount"], 500.00)
        self.assertIn("id", expense_dict)
        self.assertIn("created_at", expense_dict)
        self.assertIn("updated_at", expense_dict)


if __name__ == "__main__":
    unittest.main()
