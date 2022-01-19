from .menuItem import MenuItem
import json

class Menu:
    name: str

    def __init__(self, name: str):
        self.name = name

    def getMenu(self):
        data = [
            ("Burger", 13),
            ("Hot dog", 13),
            ("Chicken", 20),
            ("Steak", 30),
            ("French fries", 5)
        ]

        # Print the menu with fancy json style
        print(json.dumps(data, indent=4))

        # Create a dictionary of menu items
        self.items = {
            n: MenuItem(name=n, price=p) for (n, p) in data
        }

        return self.items

    def order(self):
        item = input(str(f"What do you want to order {self.name}? "))
        return item

    # Let the user know it is done and give them the price
    def processOrder(self, order: str):
        price = self.items[order].price
        print(f"You ordered {order}. The price will be ${price}. Thank you for your order {self.name}!")
