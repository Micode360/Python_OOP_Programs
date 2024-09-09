from management import Management

class Exclusive_company(Management):
    def __init__(self, name):
        super().__init__()
        self.company_name = name
        self.assets = self.load_from_file("assets.json")
        self.net_worth = self.load_net_worth()

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
            options = input("1. Add an asset.\n2. Search for an asset.\n3. View total net_worth.\n4. Exit company\nChoose (1/2/3/4): ")

            if options == "1":
                name_of_asset = input("Enter name of asset: ")
                quantity_per_asset = input("Enter quantity per asset: ")
                price_per_asset = input("Enter price per asset: ")

                # Validate quantity and price
                try:
                    quantity_per_asset = int(quantity_per_asset)
                    price_per_asset = float(price_per_asset)
                except ValueError:
                    print("Invalid input. Quantity should be an integer and price should be a number.")
                    continue

                self.add_asset({"name": name_of_asset, "quantity": quantity_per_asset, "price": price_per_asset})
                self.save_to_file('assets.json', self.assets)
                self.net_worth = self.load_net_worth()  # Update net_worth after adding asset
                print(f"Asset successfully added. Your current net worth is ${self.net_worth}")
            elif options == "2":
                choice = input("What asset are you looking for?: ")
                print(self.search_for_an_asset(choice))
            elif options == "3":
                if self.net_worth == 0:
                    print("Your account is very low")
                else:
                    print(f"Your total net worth is ${self.net_worth}")
            elif options == "4":
                print("Thank you for your time. It Was Great hearing From You.")
                break
            else:
                print("Invalid option, please choose again.")
