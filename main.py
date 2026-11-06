
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
                income_source_name = get_transaction("Enter income source name (e.g. Salary, Bonus, etc.): ")
                income.append({"income_amount": income_amount, "income_source_name": income_source_name})
                # if they did not say yes, then break
                if not get_yes_no("Add another income (yes/no): "):
                    break
        elif choice == 2:
            print("You selected Add Expense")
            while True:
                expense_amount = get_amount("Enter expense amount: ")
                expense_category = get_transaction("Enter expense category (e.g. Food, Rent, etc.): ")
                expenses.append({"expense_amount": expense_amount, "expense_category": expense_category})
                # if they did not say yes, then break
                if not get_yes_no("Add another expense (yes/no): "):
                    break
        elif choice == 3:
            summary(income, expenses)
        elif choice == 4:
            print("You selected Quit")
            break
    except ValueError:
        print("Invalid option. Please select a valid option (1-4).")
