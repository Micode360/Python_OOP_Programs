import os
import json

class File:
    @staticmethod
    def save_to_file(filename, data):
        if not os.path.exists('store'):
            os.makedirs('store')
        
        try:
            with open(f"store/{filename}", 'w') as file:
                json.dump(data, file, indent=4)
            print(f"{filename} saved")
        except IOError as e:
            print(f"Error saving {filename}: {e}")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(f"store/{filename}", "r") as file:
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
