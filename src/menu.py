from .menuItem import MenuItem
import json

class Menu:
    name: str

    def __init__(self, name: str):
        self.name = name

    def getMenu(self):
        data = [
            ("Burger", "some description",13),
            ("Hot dog", "some description", 13),
            ("Chicken", "some description", 20),
            ("Steak", "some description", 30),
            ("French fries", "some description", 5)
        ]

        # Print the menu with fancy json style
        print(json.dumps(data, indent=4))

        # Create a dictionary of menu items
        self.items = {
            n: MenuItem(name=n, description=d, price=p) for (n, d, p) in data
        }

        return self.items

    def order(self):
        item = input(str(f"What do you want to order {self.name}? "))
        return item

    # Let the user know it is done and give them the price
    def processOrder(self, order: str):
        price = self.items[order].price
        print(f"You ordered {order}. The price will be ${price}. Thank you for your order {self.name}!")
