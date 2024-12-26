"""
This service will be in charge of:
 * compare if there is enough resources quantity to make the drink
 * make the drink
 * deduct from resources the quantity used
"""


def create_beverage(beverage_name, ingredients, resources):
    for name in ingredients:
        wasted_amount = ingredients[name]
        resources[name] = resources[name] - wasted_amount
    print(f"Here is your {beverage_name}, enjoy!!")


def beverage_validations(ingredients, resources):
    for name in ingredients:
        if ingredients[name] > resources[name]:
            print(f"Sorry there is not enough {name}")
            return False
    return True


def replenish_resources(resources):
    for name, current_amount in resources.items():
        replenish_amount = int(input("input the quantity of {name} that you want to add to the machine: "))
        resources[name] = current_amount + replenish_amount