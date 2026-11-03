
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
    income_sum = sum(income_list)
    expenses_sum = sum(expenses_list)
    balance_amount = income_sum - expenses_sum
    print("You selected Summary")

    if not income_list and not expenses_list:
        print("Nothing to summarize.")
        return
    for count, earning in enumerate(income_list, start=1):
        print(f"Income Source {count}: ${earning:.2f}")
    for count, amount in enumerate(expenses_list, start=1):
        print(f'Expenses Source {count}: ${amount:.2f}')
    print(f"\nTotal income: ${float(income_sum):.2f}")
    print(f"Total expenses: ${float(expenses_sum):.2f}")
    print(f"Total balance: ${float(balance_amount):.2f}")


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
            summary(income, expenses)
        elif choice == 4:
            print("You selected Quit")
            break
    except ValueError:
        print("Invalid option. Please select a valid option (1-4).")
