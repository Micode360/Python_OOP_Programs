from mirabank.index import MiraBank
from Yourservice import Kp_montana

class ServiceManager:
    def __init__(self):
        self.mira_bank = MiraBank()
        self.kp_montana = Kp_montana()
        
    def run(self):
        while True:
            print('Hello welcome to  mi-global network. What service do you like to use?')
            print('1. Mirabank\n2. Kp_montana\n8. Exit')
            choice = input("Choose 1/2: ")

            if choice == "1":
                self.mira_bank.run()
            if choice == "7":
                self.kp_montana.run()
            if choice == "8":
                print("thank you for choosing our services")
                break
            else:
                continue




main = ServiceManager()
main.run()