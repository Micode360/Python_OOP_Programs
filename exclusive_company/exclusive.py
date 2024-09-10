from exclusive_company.management import Management
from exclusive_company.Supermarketmain import MainFunction

class Exclusive_company(Management, MainFunction):
    def __init__(self, name):
        super().__init__()
        self.company_name = name
        self.assets = self.load_from_file("assets.json")
        self.net_worth = self.load_net_worth()
        self.supermarketmain = MainFunction()
    def add_asset(self, asset_dict):
        self.assets.append(asset_dict)
        
    def search_for_an_asset(self, name):
        for asset in self.assets:
            if name.lower() == asset["name"].lower():
                return self.display_asset(asset)
        return "No asset found"
            
    def display_asset(self, asset):
        print("=="*40)
        print(f"name: {asset['name']}\nquantity: {asset['quantity']}\nprice per asset: {asset['price']}")
        print("=="*40)

    def run(self):
        while True:
            print(f"Welcome to {self.company_name}. What do you want to do?")
            options = input("a. EDC Investment.\nb. EDC Supermarket.\nc. Exit\nChoose (a/b/c): ")
            
            if options == "a":
                print(f"Welcome to {self.company_name} Investment. What do you want to do?")
                investment_options = input("1. Add an asset.\n2. Search for an asset.\n3. View total net_worth.\n4. List Assets.\n5. Exit company\nChoose (1/2/3/4/5): ")
                if investment_options == "1":
                    name_of_asset = input("Enter name of asset: ")
                    quantity_per_asset = input("Enter quantity per asset: ")
                    price_per_asset = input("Enter price per asset: ")

                    try:
                        quantity_per_asset = int(quantity_per_asset)
                        price_per_asset = float(price_per_asset)
                    except ValueError:
                        print("Invalid input. Quantity should be an integer and price should be a number.")
                        continue

                    self.add_asset({"name": name_of_asset, "quantity": quantity_per_asset, "price": price_per_asset})
                    self.save_to_file('assets.json', self.assets)
                    self.net_worth = self.load_net_worth()
                    print(f"Asset successfully added. Your current net worth is ${self.net_worth}")
                elif investment_options == "2":
                    choice = input("What asset are you looking for?: ")
                    print(self.search_for_an_asset(choice))
                elif investment_options == "3":
                    if self.net_worth == 0:
                        print("Your account is very low")
                    else:
                        print(f"Your total net worth is ${self.net_worth}")
                elif investment_options == "4":
                    print(self.assets)
                elif investment_options == "5":
                    print("Thank you for your time. It was great hearing from you.")
                    break
                else:
                    print("Invalid option, please choose again.")
            elif options == "b":
                self.supermarketmain.run()
            elif options == "c":
                print("Thank you for choosing our services")
                break
            else:
                print("Invalid option, please choose again.")

        