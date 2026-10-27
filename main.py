print("Track your spending\n")

print("1. Add Income")
print("2. Add Expense")
print("3. View Summary")
print("4. Quit")

income = []

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
                    print("Please enter a valid income amount.")
        elif choice == 2:
            print("You selected Add Expense")
        elif choice == 3:
            print("You selected View Summary")
            print(income) # Just for testing right now
            print(f"Total income: ${sum(income):.2f}")
        elif choice == 4:
            print("You selected Quit")
            break
    except ValueError:
        print("Invalid option. Please select a valid option (1-4).")
