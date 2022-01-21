from src import Menu
import time

name: str = input("What is your name? ")

menu = Menu(name)
print("Enter in the name of the item you want to select")
print("The menu options are:")
mainMenu = menu.getMenu()

order = menu.order()

# If the item the user entered is not in the main menu
if order not in mainMenu:
    print(f"Sorry, we don't have {order} in the menu.")
    exit(0x45)

# No errors then process that order baby
print("Your order has been placed.")
time.sleep(0.5)
menu.processOrder(order)
