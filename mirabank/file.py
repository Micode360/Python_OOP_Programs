import os
import json

class File:
    @staticmethod
    def save_to_file(filename, data):
        if not os.path.exists('store'):
            os.makedirs('store')
        
        with open(f"store/{filename}",'w') as file:
            json.dump(data, file, indent=4)
            return "file created"

    @staticmethod
    def load_from_file(filename):
        try:
            with open(f"store/{filename}", "r")as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"There was an error decoding the json file at {filename}")
            return []

