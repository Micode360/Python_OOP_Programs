import json
import os

class FileHandler:
    def __init__(self, filename='catalog.json'):
        self.filename = filename
        self.directory = 'exclusive_company/store'
        
        # Ensure the directory exists
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            
    def get_file_path(self):
        return os.path.join(self.directory, self.filename)


    @staticmethod
    def save_to_file(filename, data):        
        try:
            with open(f"exclusive_company/store/{filename}", 'w') as file:
                json.dump(data, file, indent=4)
            print(f"{filename} saved")
        except IOError as e:
            print(f"Error saving {filename}: {e}")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(f"exclusive_company/store/{filename}", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"{filename} not found.")
            return []
        except json.JSONDecodeError:
            print(f"There was an error decoding the json file at {filename}")
            return []
        except IOError as e:
            print(f"Error loading {filename}: {e}")
            return []

    def load_catalog(self):
        return self.load_from_file(self.filename) or []

    def save_catalog(self, catalog):
        self.save_to_file(self.filename, catalog)

    def delete_file(self):
        if os.path.exists(f"store/{self.filename}"):
            os.remove(f"store/{self.filename}")
            print(f"File {self.filename} deleted.")
        else:
            print(f"File {self.filename} does not exist.")
