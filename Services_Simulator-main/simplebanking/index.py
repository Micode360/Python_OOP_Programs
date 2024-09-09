class SimpleBanking:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance is ${self.balance}.")

    def run(self):
        while True:
            print('Welcome to Simple Banking. What would you like to do?')
            print('1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit')
            choice = input("Choose 1/2/3/4: ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                self.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(amount)
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Thank you for using Simple Banking.")
                break
            else:
                print("Invalid choice, please try again.")
