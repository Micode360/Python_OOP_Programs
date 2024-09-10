import re
from file import File

class Deposit(File):
    def __init__(self):
          super().__init__()
          #load accounts
          self.accounts = self.load_from_file("accounts.json")

    def validate_account(self, account_no):
        # Define regex pattern for a string of exactly 10 digits
        pattern = r'^\d{10}$'

        # Check if account_no matches the pattern
        if not re.match(pattern, account_no):
            print("Invalid account number. It must be a string of exactly 10 numeric characters.")
            return False

        # Check if the account number already exists in the accounts
        for account in self.accounts:
            if account.get("account_number") == account_no:
                return True

            
    def save_to_account(self, account_no, amount):
        # Define regex pattern for a positive decimal number with optional decimal part
        amount_pattern = r'^\d+(\.\d{1,2})?$'

        # Validate that amount matches the pattern
        if not re.match(amount_pattern, amount):
            print("Invalid amount. It must be a positive number with up to 2 decimal places.")
            return False

        for account in self.accounts:
            if account["account_number"] == account_no:
                account["money"] = str(int(account["money"]) + int(amount))  
        else:
            self.save_to_file("accounts.json", self.accounts)
        
        print("Account number not found.")
        return False

    def run(self):
        while True:
            account_no = input("Enter your account number: ")

            is_validated = self.validate_account(account_no=account_no)

            if is_validated:
                 amount = input("Enter amount you want to deposit: ")
                 self.save_to_account(account_no=account_no, amount=amount)
                 print(f"{"=="*24}\n{amount} saved into your account.\n{"=="*24}")
                 break
            else:
                 print(f"{"=="*24}\nNo such account. Create an account with our services.\n{"=="*24}")
                 break