# from mirabank.index import MiraBank
# class ServiceManager:
#     def __init__(self):
#         self.mira_bank = MiraBank()
        
#     def run(self):
#         while True:
#             print('Hello welcome to  mi-global network. What service do you like to use?')
#             print('1. Mirabank\n2. Exit')
#             choice = input("Choose 1/2: ")

#             if choice == "1":
#                 self.mira_bank.run()
#             if choice == "2":
#                 print("thank you for choosing our services")
#                 break
#             else:
#                 continue




# main = ServiceManager()
# main.run()



from mirabank.index import MiraBank
from simplebanking.index import SimpleBanking

class ServiceManager:
    def __init__(self):
        self.mira_bank = MiraBank()
        self.simple_banking = SimpleBanking()

    def run(self):
        while True:
            print('Hello, welcome to mi-global network. What service would you like to use?')
            print('1. MiraBank\n2. Exit')
            choice = input("Choose 1/2/3: ")

            if choice == "1":
                self.mira_bank.run()
            elif choice == "2":
                print("Thank you for choosing our services.")
                break
            else:
                print("Invalid choice, please try again.")

main = ServiceManager()
main.run()
