from src import Menu
import time

name: str = input("What is your name? ")

menu = Menu(name)
print("Enter in the name of the item you want to sellect")
print(f"The menu options are:")
mainMenu = menu.getMenu()

order = menu.order()

if order not in mainMenu:
    print("Sorry, we don't have that item.")
else:
    print("Your order has been placed.")
    time.sleep(0.5)
    menu.processOrder(order)
