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
                    additional_income = input("Add another income (y/n): ")
                    while additional_income.lower() == "y":
                        new_income = float(input("Enter income amount: "))
                        if new_income <= 0:
                            print("Income amount must be greater than 0.")
                            continue
                        income.append(new_income)
                        additional_income = input("Add another income (y/n): ")
                        # Need to handle case where user types anything but y or n
                    else:
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
