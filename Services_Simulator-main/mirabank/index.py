from simplebanking.index import SimpleBanking
class MiraBank:
    def run(self):
        self.simple_banking = SimpleBanking()
        while True:
            print('Hello welcome to Mira Bank. What what bring you to our services?')
            print('1. Option 1\n2. Exit')
            choice = input("Choose 1/2: ")

            if choice == "1":
                self.simple_banking.run()
            if choice == "2":
                print("Thank you for choosing our services")
                break
            else:
                continue
