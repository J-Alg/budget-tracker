def menu():
    print("1. Income")
    print("2. Expenses")
    print("3. Summary")
    print("4. Quit")

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

def summary(income_list, expenses_list):
    income_sum = sum([i.get("income_amount") for i in income_list])
    expenses_sum = sum(e.get("expense_amount") for e in expenses_list)
    balance_amount = income_sum - expenses_sum
    print("You selected Summary")

    if not income_list and not expenses_list:
        print("Nothing to summarize.")
        return
    for earning in income_list:
        print(f"Income: {earning.get('income_source_name')} - ${earning.get('income_amount'):.2f}")
    for amount in expenses_list:
        print(f'Expenses: {amount.get("expense_category")} - ${amount.get("expense_amount"):.2f}')
    print(f"\nTotal income: ${float(income_sum):.2f}")
    print(f"Total expenses: ${float(expenses_sum):.2f}")
    print(f"Total balance: ${float(balance_amount):.2f}")

def get_transaction(type_name):
    while True:
        transaction = input(type_name).upper().strip()
        if transaction:
            return transaction
        else:
            print("Invalid input. Please enter a valid transaction name.")



income = []
expenses = []

menu()
while True:
    choice = input("\nPlease select an option (1-4): ")
    try:
        # Makes sure the input is an integer. If not, ValueError is raised
        choice = int(choice)
        # Check if the choice is within the valid range
        if choice < 1 or choice > 4:
            print("Invalid option. Please select a valid option (1-4).")
        elif choice == 1:
            while True:
                # Ask user for income amount
                income_amount = get_amount("Enter income amount: ")
                # Ask user for income source name
                income_source_name = get_transaction("Enter income source name (e.g. Salary, Bonus, etc.): ")
                # Append income and source name to the income list
                income.append({"income_amount": income_amount, "income_source_name": income_source_name})
                # if they did not say yes, then break
                if not get_yes_no("Add another income (yes/no): "):
                    break
        elif choice == 2:
            while True:
                # Ask user for expense amount
                expense_amount = get_amount("Enter expense amount: ")
                # Ask user for expense category
                expense_category = get_transaction("Enter expense category (e.g. Food, Rent, etc.): ")
                # Append expense amount and category to the expenses list
                expenses.append({"expense_amount": expense_amount, "expense_category": expense_category})
                # if they did not say yes, then break
                if not get_yes_no("Add another expense (yes/no): "):
                    break
        elif choice == 3:
            # Show the user a breakdown of their income and expenses while also displaying the
            # total income and expenses and balance after expenses
            summary(income, expenses)
        elif choice == 4:
            # End program
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid option. Please select a valid option (1-4).")
