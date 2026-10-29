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
                try:
                    new_income = float(input("Enter income amount: "))
                    if new_income <= 0:
                        print("Income amount must be greater than 0.")
                        continue
                    income.append(new_income)
                    while True:
                        add_additional_incomes = input("Add another income (y/n): ").strip().lower()
                        if add_additional_incomes in ["y", "yes"]:
                            break
                        elif add_additional_incomes in ["n", "no"]:
                            break
                        else:
                            print("Invalid option. Please select 'y' or 'n'.")
                    if add_additional_incomes in ["n", "no"]:
                        break
                except ValueError:
                    print("Please enter a valid income amount. (example: 100.00)")
        elif choice == 2:
            print("You selected Add Expense")
            while True:
                try:
                    add_expense = float(input("Enter expense amount: "))
                    if add_expense <= 0:
                        print("Expense amount must be greater than 0.")
                        continue
                    expenses.append(add_expense)
                    while True:
                        add_additional_expense = input("Add another expense (y/n): ").strip().lower()
                        if add_additional_expense in ["y", "yes"]:
                            break
                        elif add_additional_expense in ["n", "no"]:
                            break
                        else:
                            print("Invalid option. Please select 'y' or 'n'.")
                    if add_additional_expense in ["n", "no"]:
                        break
                except ValueError:
                    print("Please enter a valid expense amount. (example: 100.00)")
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
