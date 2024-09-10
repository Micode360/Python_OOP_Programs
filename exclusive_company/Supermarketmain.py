from exclusive_company.SupermarketAdmin import Admin
from exclusive_company.Supermarketstore import Store

class MainFunction(Admin, Store):
    def main():
        print("Welcome to the Store Management System!")
    def run(self):
        while True:
            print("\n1. Admin Interface")
            print("2. Store Interface")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                # Admin authentication
                password = input("Enter admin keyword to proceed: ")
                if password.lower() == "admin":
                    admin = Admin()
                    admin.add_inventory_interface()
                else:
                    print("Incorrect keyword. Access denied.")
            elif choice == "2":
                store = Store()
                
                while True:
                    print("\nWelcome to the Store!")
                    print("1. View Store Catalog")
                    print("2. Search for an Item")
                    print("3. Add Item to Cart")
                    print("4. View Cart")
                    print("5. Checkout")
                    print("6. Exit")
                    
                    store_choice = input("Choose an option: ")
                    
                    if store_choice == "1":
                        store.display_catalog()
                    elif store_choice == "2":
                        name = input("Enter the item name to search: ")
                        item = store.search_item(name)
                        if item:
                            print(f"Found item - Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")
                        else:
                            print(f"Item {name} not found.")
                    elif store_choice == "3":
                        name = input("Enter the item name to add to cart: ")
                        quantity = int(input("Enter the quantity: "))
                        store.add_to_cart(name, quantity)
                    elif store_choice == "4":
                        store.view_cart()
                    elif store_choice == "5":
                        store.checkout()
                    elif store_choice == "6":
                        print("Exiting the program. Thank you!")
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
            elif choice == "3":
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    if __name__ == "__main__":
        main()
