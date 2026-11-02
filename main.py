
def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid option. Please select 'yes' or 'no'.")

def get_amount(prompt):
    while True:
        try:
            source_amount = float(input(prompt))
            if source_amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return source_amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("Track your spending\n")
print("1. Add Income")
print("2. Add Expense")
print("3. View Summary")
print("4. Quit")

income = [] # Later we can store income in a dictionary. Giving the user the option to give income source name and amount
expenses = [] # Later we can store expenses in a dictionary. Giving the user the option to give expense category and amount

while True:
    choice = input("\nPlease select an option (1-4): ")
    try:
        choice = int(choice)
        if choice < 1 or choice > 4:
            print("Invalid option. Please select a valid option (1-4).")
        elif choice == 1:
            print("You selected Add Income")
            while True:
                income_amount = get_amount("Enter income amount: ")
                income.append(income_amount)
                # if they did not say yes, then break
                if not get_yes_no("Add another income (yes/no): "):
                    break
        elif choice == 2:
            print("You selected Add Expense")
            while True:
                expense_amount = get_amount("Enter expense amount: ")
                expenses.append(expense_amount)
                # if they did not say yes, then break
                if not get_yes_no("Add another expense (yes/no): "):
                    break
        elif choice == 3:
            total_income = sum(income)
            total_expenses = sum(expenses)
            balance = total_income - total_expenses
            warning = "You have a negative balance. Consider adding more income or reducing expenses."
            print("You selected View Summary\n")
            if not income and not expenses:
                print("Nothing to summarize yet.")
            if income and not expenses:
                count = 0
                for earning in income:
                    count += 1
                    print(f"Income Source {count}: ${earning:.2f}")
                print(f"\nTotal income: ${total_income:.2f}")
                print(f"Total expenses: ${total_expenses:.2f}")
                print(f"Total balance: ${balance:.2f} {warning if balance < 0 else ''}\n")
            if expenses and not income:
                count = 0
                for expense in expenses:
                    count += 1
                    print(f"Expense Source {count}: ${expense:.2f}")
                print(f"\nTotal income: ${total_income:.2f}")
                print(f"Total expenses: ${total_expenses:.2f}")
                print(f"Total balance: ${balance:.2f} {warning if balance < 0 else ''}")
            if income and expenses:
                income_count = 0
                expense_count = 0
                for earning in income:
                    income_count += 1
                    print(f"Income Source {income_count}: ${earning:.2f}")
                for expense in expenses:
                    expense_count += 1
                    print(f"Expense Source {expense_count}: ${expense:.2f}")
                print(f"\nTotal income: ${total_income:.2f}")
                print(f"Total expenses: ${total_expenses:.2f}")
                print(f"Total balance: ${balance:.2f} {warning if balance < 0 else ''}")
        elif choice == 4:
            print("You selected Quit")
            break
    except ValueError:
        print("Invalid option. Please select a valid option (1-4).")
