from .menuItem import MenuItem
import json

class Menu:
    name: str
    data: list = []

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

        self.data = data

        print(json.dumps(data, indent=4))

        self.items = {
            n: MenuItem(name=n, description=d, price=p) for (n, d, p) in data
        }

        return self.items

    def order(self):
        item = input(str(f"What do you want to order {self.name}? "))
        return item

    def processOrder(self, order: str):
        print(f"You ordered {order}. The price will be ${self.items.get(order, None).price}. Thank you for your order {self.name}!")
