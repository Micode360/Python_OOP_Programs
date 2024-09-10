from mirabank.deposit import Deposit
from mirabank.check_balance import Check_Balance
from mirabank.create_account import Create_Account
from mirabank.delete_account import Delete_Account
from mirabank.account_info import Account_Info

class MiraBank:
    def __init__(self):
        self.create_account = Create_Account()
        self.deposit = Deposit()
        self.check_balance = Check_Balance()
        self.delete_account = Delete_Account()
        self.account_info = Account_Info()

    def run(self):
        while True:
            print('Hello welcome to Mira Bank. What what bring you to our services?')
            print('1. Create an account.\n2. Deposit into account.\n3. Check your account balance.\n4. View your account information\n5. Delete your Account\n6. Exit')
            choice = input("Choose 1/2/3/4/5: ")

            if choice == "1":
                self.create_account.run()
            if choice == "2":
                self.deposit.run()
            if choice == "3":
                self.check_balance.run()
            if choice == "4":
                self.account_info.run()
            if choice == "5":
                self.delete_account.run()
            if choice == "6":
                print("Thank you for choosing our services")
                break
            else:
                continue