from deposit import Deposit
from file import File

class Check_Balance(File):
    def __init__(self):
          super().__init__()
          self.accounts = self.load_from_file("accounts.json")
          self.from_deposit = Deposit()

    def get_balance(self, account_no):
         for account in self.accounts:
              if account["account_number"] == account_no:
                   print(f"{"=="*24}\nYour account balance is ${account["money"]}\n{"=="*24}")
    
    def run(self):
        while True:
            account_no = input("Enter your account number: ")

            is_validated = self.from_deposit.validate_account(account_no=account_no)

            if is_validated:
                 self.get_balance(account_no=account_no)
                 break
            else:
                 print(f"{"=="*24}\nNo such account. Create an account with our services.{"=="*24}\n")
                 break