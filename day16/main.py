from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def process_beverage(coffee_name,  menu, money_machine):
    coffee_choice = menu.find_drink(coffee_name)
    if coffee_choice and coffee_maker.is_resource_sufficient(coffee_choice):
        if money_machine.make_payment(coffee_choice.cost):
            coffee_maker.make_coffee(coffee_choice)


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    menu_items = menu.get_items()
    choice = input(f"What would you like? {menu_items}: \n").lower()
    match choice:
        case "report":
            coffee_maker.report()
            money_machine.report()
        case "off":
            is_on = False
        case "replenish":
            coffee_maker.replenish_resources()
        case _:
            process_beverage(choice, menu, money_machine)
