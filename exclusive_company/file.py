import os
import json

class File:
    @staticmethod
    def save_to_file(filename, data):
        directory = 'exclusive_company/store'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        try:
            file_path = os.path.join(directory, filename)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"{filename} saved")
        except IOError as e:
            print(f"Error saving {filename}: {e}")

    @staticmethod
    def load_from_file(filename):
        file_path = os.path.join('exclusive_company/store', filename)
        try:
            with open(file_path, 'r') as file:
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
