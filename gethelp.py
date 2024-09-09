class Kp_montana:
    def __init__(self):
        self.balance = 10000  # Example initial balance

    def run(self):
        while True:
            print("Kp_montana Service:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit to Main Menu")
            choice = input("Choose 1/2/3/4: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance is: ${self.balance}")
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is: ${self.balance}")
            else:
                print("Invalid or insufficient amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

