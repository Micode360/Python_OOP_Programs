from exclusive_company.Supermarketfile import FileHandler

class Store(FileHandler):
    def __init__(self, filename='catalog.json'):
        super().__init__(filename)
        self.catalog = self.load_catalog()
        self.cart = []

    def display_catalog(self):
        print("Store Catalog:")
        for item in self.catalog:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")

    def search_item(self, name):
        for item in self.catalog:
            if item["name"].lower() == name.lower():
                return item
        return None
    
    def buy_item(self, name, quantity):
        item = self.search_item(name)
        if item:
            if item["quantity"] >= quantity:
                total_cost = item["price"] * quantity
                item["quantity"] -= quantity
                self.save_catalog(self.catalog)  # Update the catalog file
                print(f"Purchased {quantity} {name}(s) for ${total_cost:.2f}.")
            else:
                print(f"Sorry, only {item['quantity']} {name}(s) available.")
        else:
            print(f"Item {name} not found in catalog.")

    def add_to_cart(self, name, quantity):
        item = self.search_item(name)
        if item:
            if item["quantity"] >= quantity:
                self.cart.append({"name": name, "quantity": quantity, "price": item["price"]})
                item["quantity"] -= quantity
                self.save_catalog(self.catalog)  # Update the catalog file
                print(f"Added {quantity} {name}(s) to cart.")
            else:
                print(f"Sorry, only {item['quantity']} {name}(s) available.")
        else:
            print(f"Item {name} not found in catalog.")
    
    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        print("Your Cart:")
        for item in self.cart:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price per unit: ${item['price']:.2f}, Total price: ${item['price'] * item['quantity']:.2f}")
    
    def checkout(self):
        if not self.cart:
            print("Cart is empty. Nothing to checkout.")
            return
        
        # Collect customer information
        customer_name = input("Enter your name: ")
        customer_address = input("Enter your address: ")
        customer_phone = input("Enter your phone number: ")

        total_cost = sum(item['price'] * item['quantity'] for item in self.cart)
        print(f"\nTotal amount due: ${total_cost:.2f}")
        print(f"Customer Name: {customer_name}")
        print(f"Customer Address: {customer_address}")
        print(f"Customer Phone: {customer_phone}")

        self.cart.clear()
        print("Thank you for shopping with us!")
