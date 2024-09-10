from exclusive_company.Supermarketfile import FileHandler

class Admin(FileHandler):
    def __init__(self, filename='catalog.json'):
        self.file_handler = FileHandler(filename)
        self.catalog = self.file_handler.load_catalog()

    def display_catalog(self):
        print("Current Catalog:")
        for item in self.catalog:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")

    def add_item(self, name, quantity, price):
        for item in self.catalog:
            if item["name"].lower() == name.lower():
                item["quantity"] += quantity
                self.file_handler.save_catalog(self.catalog)
                print(f"Updated {name} quantity to {item['quantity']}.")
                return
        
        new_item = {"name": name, "quantity": quantity, "price": price}
        self.catalog.append(new_item)
        self.file_handler.save_catalog(self.catalog)
        print(f"Added new item {name} to catalog.")
    
    def update_item(self, name, quantity=None, price=None):
        for item in self.catalog:
            if item["name"].lower() == name.lower():
                if quantity is not None:
                    item["quantity"] = quantity
                if price is not None:
                    item["price"] = price
                self.file_handler.save_catalog(self.catalog)
                print(f"Updated {name}: Quantity = {item['quantity']}, Price = ${item['price']:.2f}.")
                return
        
        print(f"Item {name} not found in catalog.")

    def remove_item(self, name):
        self.catalog = [item for item in self.catalog if item["name"].lower() != name.lower()]
        self.file_handler.save_catalog(self.catalog)
        print(f"Removed item {name} from catalog.")

    def calculate_price(self, name, quantity):
        item = next((item for item in self.catalog if item["name"].lower() == name.lower()), None)
        if item:
            return item["price"] * quantity
        print(f"Item {name} not found.")
        return 0.0

    def add_inventory_interface(self):
        while True:
            print("\nAdmin Inventory Management")
            print("1. Display Catalog")
            print("2. Add New Item")
            print("3. Update Item")
            print("4. Remove Item")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.display_catalog()
            elif choice == "2":
                name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per item: "))
                self.add_item(name, quantity, price)
            elif choice == "3":
                name = input("Enter item name to update: ")
                quantity = input("Enter new quantity (leave blank if no change): ")
                price = input("Enter new price (leave blank if no change): ")
                quantity = int(quantity) if quantity else None
                price = float(price) if price else None
                self.update_item(name, quantity, price)
            elif choice == "4":
                name = input("Enter item name to remove: ")
                self.remove_item(name)
            elif choice == "5":
                print("Exiting Admin Interface.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
