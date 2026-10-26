print("Track your spending\n")

print("1. Add Income")
print("2. Add Expense")
print("3. View Summary")
print("4. Quit")

while True:
    choice = input("\nPlease select an option (1-4): ")
    try:
        choice = int(choice)
        if choice < 1 or choice > 4:
            print("Invalid option. Please select a valid option (1-4).")
        elif choice == 1:
            print("You selected Add Income")
        elif choice == 2:
            print("You selected Add Expense")
        elif choice == 3:
            print("You selected View Summary")
        elif choice == 4:
            print("You selected Quit")
            break
    except ValueError:
        print("Invalid option. Please select a valid option (1-4).")
