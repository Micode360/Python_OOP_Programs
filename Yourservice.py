class Kp_montanta:
    def __init__(self):
        self.balance = 1000  # Example initial balance

    def run(self):
        while True:
            print("MiraBank Service:")
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
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: $"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is: ${self.balance}")
        else:
            print("Invalid or insufficient amount.")

class TransactionService:
    def __init__(self):
        self.transactions = []

    def run(self):
        while True:
            print("Transaction Service:")
            print("1. Record Transaction")
            print("2. View Transactions")
            print("3. Exit to Main Menu")
            choice = input("Choose 1/2/3: ")

            if choice == "1":
                self.record_transaction()
            elif choice == "2":
                self.view_transactions()
            elif choice == "3":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def record_transaction(self):
        transaction_type = input("Enter transaction type (e.g., Deposit, Withdrawal): ")
        amount = float(input("Enter amount: $"))
        self.transactions.append((transaction_type, amount))
        print(f"Recorded {transaction_type} of ${amount}.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print("Transaction History:")
            for t in self.transactions:
                print(f"Type: {t[0]}, Amount: ${t[1]}")

class ServiceManager:
    def __init__(self):
        self.mira_bank = MiraBank()
        self.transaction_service = TransactionService()

    def run(self):
        while True:
            print("Hello welcome to  mi-global network. What service do you like to use?")
            print("1. MiraBank")
            print("2. Transaction Service")
            print("3. Exit")
            choice = input("Choose 1/2/3: ")

            if choice == "1":
                self.mira_bank.run()
            elif choice == "2":
                self.transaction_service.run()
            elif choice == "3":
                print("Thank you for using the service. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Execution
if __name__ == "__main__":
    manager = ServiceManager()
    manager.run()
