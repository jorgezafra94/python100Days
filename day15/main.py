"""
This is the coffee machine
"""
from report_service import report
from menu_service import beverage_validations, create_beverage, replenish_resources
from payment_service import get_user_payment, payment_validations, process_payment

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_beverage(beverage_name):
    recipie = MENU[beverage_name]
    ingredients = recipie["ingredients"]
    beverage_cost = recipie["cost"]

    # check resources for beverage
    if not beverage_validations(ingredients, resources):
        return

    # check money
    user_money = get_user_payment()
    if not payment_validations(user_money, beverage_cost):
        return

    global profit
    profit += process_payment(user_money, beverage_cost)
    create_beverage(beverage_name, ingredients, resources)


is_on = True
while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): \n").lower()
    match choice:
        case "report":
            report(resources, profit)
        case "espresso" | "latte" | "cappuccino":
            process_beverage(choice)
        case "replenish":
            replenish_resources(resources)
        case "off":
            is_on = False
        case _:
            print("We can not create that beverage, apologies!")
