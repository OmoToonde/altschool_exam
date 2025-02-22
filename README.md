# Altschool Exam - Expense Tracker 📝

A simple **Expense Tracker** project for the **AltSchool Data Engineering First Semester Project Exam**.  
This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python by implementing an `Expense` class and an `ExpenseDatabase` class.

---

## 🚀 Features
- Create and manage expenses with **UUIDs and timestamps**.
- Store multiple expenses and retrieve them by **ID or title**.
- Update expense details dynamically.
- Remove expenses from the database.
- Convert expense data to **JSON-compatible dictionary format**.

---

## 🛠️ Installation
To use this project, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/OmoToonde/altschool_exam.git
   cd altschool_exam
   ```

---

## 🛠️ Step 2: Set Up a Virtual Environment (Optional but Recommended)
Creating a virtual environment helps manage dependencies and avoid conflicts with system-wide Python packages.

### **For Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

### **For Mac**
```sh
python3 -m venv venv
source venv/bin/activate
```

---

## 📝 Step 3: Running the Expense Tracker
To run the program, execute the following command in your terminal:
```sh
python expense_tracker.py
```

---

## 🏗️ Step 4: Adding and Managing Expenses
To add expenses to the database, use the following Python script:

```python
from expense_tracker import Expense, ExpenseDatabase

# Initialize the database
db = ExpenseDatabase()

# Create new expenses
expense1 = Expense("Groceries", 50.25)
expense2 = Expense("Transport", 15.75)

# Add expenses to the database
db.add_expense(expense1)
db.add_expense(expense2)

# Print all expenses
print(db.to_dict())  # Displays the list of expenses in dictionary format
```

---

## ✏️ Step 5: Updating an Expense
You can update an expense’s **title** or **amount** dynamically using the `update()` method.

```python
# Update only the amount
expense1.update(amount=60.00)  # Change amount to 60
print(expense1.to_dict())  # Confirm update

# Update only the title
expense1.update(title="Supermarket Groceries")
print(expense1.to_dict())  # Confirm updated title
```

---

## ❌ Step 6: Removing an Expense
To remove an expense from the database, use the `remove_expense()` method with the **expense ID**.

```python
# Remove an expense by ID
db.remove_expense(expense1.id)

# Print the updated expense list to confirm removal
print(db.to_dict())  # Expense should be removed from the list
```

---

## 🧪 Step 7: Running Tests
To ensure that the **Expense Tracker** application is functioning correctly, run the **unit tests** included in the project.

### ✅ Running the Tests
Use the following command in your terminal:
```sh
python -m unittest test_expense_tracker.py
```

### ✅ Expected Output:
If all tests pass successfully, you should see:
```sh
OK
```
