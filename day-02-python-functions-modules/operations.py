from models import Expense, InvalidAmount


def add_expense(expenses, **kwargs):
    description = kwargs.get("description")
    amount = kwargs.get("amount")

    if amount < 0:
        raise InvalidAmount("Amount cannot be negative")

    expense = Expense(description, amount)
    expenses.append(expense)


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found")
        return

    for expense in expenses:
        print(f"{expense.description} - ₹{expense.amount}")


def calculate_total(*expenses):
    total = 0

    for expense in expenses:
        total += expense.amount

    return total


def find_highest(expenses):
    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense.amount > highest.amount:
            highest = expense

    return highest