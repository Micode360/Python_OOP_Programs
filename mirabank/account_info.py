from mirabank.deposit import Deposit
from mirabank.file import File

class Account_Info(File):
    def __init__(self):
          super().__init__()
          self.accounts = self.load_from_file("accounts.json")
          self.from_deposit = Deposit()

    def account_information(self, account_no):
        for account in self.accounts:
            if account.get("account_number") == account_no:
                    print(f"{"=="*24}\nACCOUNT INFORMATION:\nName:{account["name"]}\nEmail:{account["email"]}.\nAccount number:{account["account_number"]}\n{"=="*24}")
        
    def run(self):
        while True:
            account_no = input("Enter your account number: ")
            is_validated = self.from_deposit.validate_account(account_no=account_no)

            if is_validated:
                 self.account_information(account_no=account_no)
                 break
            else:
                 print(f"{"=="*24}\nNo such account. Create an account with our services.{"=="*24}\n")
                 break