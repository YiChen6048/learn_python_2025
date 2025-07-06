# Beginner level ATM system simulation
# Skills practiced: Control Structures, Function Definition, User Input & Output, Basic Arithmetic Operations

def atm_system():
    balance = 0
    
    while True:
        print("Welcome to atm system.")
        print("1. deposit")
        print("2. withdraw")
        print("3. check balance")
        print("4. exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Deposited {amount}. New balance is {balance:.2f}.")
            else:
                print("Deposit amount must be positive.")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                balance -= amount
                print(f"Withdrew {amount}. New balance is {balance}.")

        elif choice == '3':
            print(f"Current balance is {balance}.")

        elif choice == '4':
            print("Exiting ATM system.")
            break
        else:
            print("Invalid choice. Please try again.")


atm_system()# This function simulates a simple ATM system where users can deposit, withdraw, and check their balance
# It handles basic input validation and provides feedback on transactions.