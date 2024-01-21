# Basic ATM System

balance = 5000.00

while True:
    print("Welcome to ATM")
    print("\n1. Check Your Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your balance is: ${balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print("Not enough balance. Cannot withdraw.")
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn. Remaining balance: ${balance:.2f}")
    elif choice == "3":
        amount = float(input("Enter the amount to deposit: $"))
        if amount < 0:
            print("Invalid deposit amount.")
        else:
            balance += amount
            print(f"${amount:.2f} deposited. New balance: ${balance:.2f}")
    elif choice == "4":
        print("Thanks for using the ATM. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
