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

        print(json.dumps(data, indent=4))

        items = {
            n: MenuItem(name=n, description=d, price=p) for (n, d, p) in data
        }

        return items

    def order(self):
        item = input(str(f"What do you want to order {self.name}? "))
        return item

    # def processOrder(self, order: MenuItem()):
        # print(f"{self.name} has ordered {order.name}")
        # return item
