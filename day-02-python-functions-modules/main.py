from operations import (
    add_expense,
    view_expenses,
    calculate_total,
    find_highest
)

from models import InvalidAmount


expenses = []


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Find Highest Expense")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:

            try:
                description = input("Enter Expense: ")
                amount = int(input("Enter Amount: "))

                add_expense(
                    expenses,
                    description=description,
                    amount=amount
                )

                print("Expense added successfully")

            except ValueError:
                print("Amount must be a number")

            except InvalidAmount as e:
                print(e)

        elif choice == 2:

            view_expenses(expenses)

        elif choice == 3:

            total = calculate_total(*expenses)
            print(f"Total: ₹{total}")

        elif choice == 4:

            highest = find_highest(expenses)

            if highest is None:
                print("No expenses found")
            else:
                print(
                    f"Highest: {highest.description} - ₹{highest.amount}"
                )

        elif choice == 5:

            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid menu number")