import re
import random
from file import File

class Create_Account(File):
    def __init__(self):
        super().__init__()
        #load accounts
        self.accounts = self.load_from_file("accounts.json")

    def generate_account_number(self):
        return str(random.randint(1000000000, 9999999999))
    
    def validation(self, name, email):
        message = {}

        # Check if name or email is empty
        if not name.strip():
            message["name"] = "Name cannot be empty."
        elif not name.isalpha():
            message["name"] = "Name must contain only alphabets."

        if not email.strip():
            message["email"] = "Email cannot be empty."
        elif email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            message["email"] = "Invalid email format."

        # Check if the name or email already exists in the accounts
        for account in self.accounts:
            if account["name"] == name:
                message["name"] = "Such name already exists."
            if account["email"] == email:
                message["email"] = "Another account has this email."

        # Print error messages if there are any
        if message:
            print(f'{"="*24}\nERROR MESSAGE:\nname: {message.get("name", "No issue")}\nemail: {message.get("email", "No issue")}\n{"="*24}')
            return False

        return True
    
    def run(self):
            while True:
                name = input('Write the name of your account: ')
                email = input ('Enter your email: ')

                valiate_user = self.validation(name=name, email=email)

                if valiate_user is False:
                    continue

                account_no = self.generate_account_number()
                new_user = {"name": name, "email": email, "account_number": account_no, "money" : "0"}

                # add new file
                self.accounts.append(new_user)

                # Save to json file
                saved = self.save_to_file("accounts.json", self.accounts)
                if saved == "file created":
                    print(f"{"=="*24}\nYour account has been created.\nYour account information is:\nname:{name}\nemail:{email}\naccount_no:{account_no}\n{"=="*24}")
                    break






