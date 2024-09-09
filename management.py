from file import File

class Management(File):
    def __init__(self):
        super().__init__()

    def load_net_worth(self):
        total_net_worth = 0
        assets = self.load_from_file('assets.json')
        if assets:
            for asset in assets:
                try:
                    total_net_worth += float(asset["price"]) * int(asset["quantity"])
                except (ValueError, KeyError):
                    print(f"Invalid data found in assets file: {asset}")
        return total_net_worth
