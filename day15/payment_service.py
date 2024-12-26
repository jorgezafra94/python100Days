"""
This service will be in charge of:
* compare if there is enough money to make the drink otherwise refund it
* give change depending on the amount
* add info to the profit
"""


def get_user_payment():
    print("Please insert the coins")
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickles_amount = int(input("How many nickles?: "))
    pennies_amount = int(input("How many pennies?: "))

    quarters = 0.25 * quarters_amount
    dimes = 0.1 * dimes_amount
    nickles = 0.05 * nickles_amount
    pennies = 0.01 * pennies_amount

    return quarters + dimes + nickles + pennies


def payment_validations(user_payment_amount, drink_cost):
    if user_payment_amount < drink_cost:
        return False, f"There is not enough money to make this drink \n ${user_payment_amount} returned!"
    return True, ""


def process_payment(user_payment_amount, drink_cost):
    if user_payment_amount == drink_cost:
        print("Thank you for your payment, creating beverage .......")
    else:
        change = user_payment_amount - drink_cost
        print(f"Thank you for your payment, Here is your change ${change}, creating beverage .......")
    return drink_cost
