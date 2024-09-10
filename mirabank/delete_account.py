from deposit import Deposit
from file import File

class Delete_Account(File):
    def __init__(self):
          super().__init__()
          self.accounts = self.load_from_file("accounts.json")
          self.from_deposit = Deposit()

    def delete_account(self, account_no):
        for account in self.accounts:
            if account.get("account_number") == account_no:
                # Remove the account from the list
                self.accounts.remove(account)
                
                # Save the updated list to the file
                saved = self.save_to_file("accounts.json", self.accounts)
                if saved == "file created":
                    print(f"{"=="*24}\nAccount with number {account_no} has been deleted.\n{"=="*24}")
                return True
        
    def run(self):
        while True:
            account_no = input("Enter your account number: ")

            is_validated = self.from_deposit.validate_account(account_no=account_no)

            if is_validated:
                 self.delete_account(account_no=account_no)
                 break
            else:
                 print(f"{"=="*24}\nNo such account. Create an account with our services.{"=="*24}\n")
                 break