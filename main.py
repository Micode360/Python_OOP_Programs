from mirabank.index import MiraBank
class ServiceManager:
    def __init__(self):
        self.mira_bank = MiraBank()
        
    def run(self):
        while True:
            print('Hello welcome to mi-global network. What service do you like to use?')
            print('1. Mirabank\n2. Exit')
            choice = input("Choose 1/2: ")

            if choice == "1":
                self.mira_bank.run()
            if choice == "2":
                print("thank you for choosing our services")
                break
            else:
                continue




main = ServiceManager()
main.run()