from mirabank.index import MiraBank
from exclusive_company.exclusive import Exclusive_company

class ServiceManager:
    def __init__(self):
        self.mira_bank = MiraBank()
        self.exclusive_company = Exclusive_company("EDC International")
        
    def run(self):
        while True:
            print('Hello, welcome to the mi-global network. What service would you like to use?')
            print('1. Mirabank\n2. Exclusive_company\n8. Exit')
            choice = input("Choose 1/2/8: ")

            if choice == "1":
                self.mira_bank.run()
            elif choice == "2":
                self.exclusive_company.run()
            elif choice == "8":
                print("Thank you for choosing our services")
                break
            else:
                print("Invalid option, please choose again.")

if __name__ == "__main__":
    main = ServiceManager()
    main.run()
