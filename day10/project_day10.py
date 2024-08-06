"""
project Python calculator
"""
from art import logo
import re


def addition(num1, num2):
    """
    this function adds two numbers
    :param num1: int or float number
    :param num2: int or float number
    :return: result of the addition of two input numbers
    """
    return num1 + num2


def subtraction(num1, num2):
    """
    this function subtracts one number from another
    :param num1: int or float number
    :param num2: int or float number
    :return: result of the subtraction of two input numbers
    """
    return num1 - num2


def multiplication(num1, num2):
    """
    this function multiply two numbers
    :param num1: int or float number
    :param num2: int or float number
    :return: result of the multiplication of two input numbers
    """
    return num1 * num2


def division(num1, num2):
    """
    this function divide two numbers
    :param num1: int or float number
    :param num2: int or float number
    :return: result of the division of two input numbers
    """
    return num1 / num2


def validate_number(number):
    """
    this function is to validate that the input number is a number
    :param number: string number to validate
    :return: float or int number or message in case it is not a valid number
    """
    regex = r"[-]?[0-9]*[.]?[0-9]*"
    pattern = re.compile(regex)
    if re.fullmatch(pattern, number):
        if "." in number:
            return float(number)
        else:
            return int(number)
    else:
        return f"'{number}' is NOT an valid number"


def validate_operation(operation, op_dict):
    """
    validate the operation entered by the user
    :param operation: operation entered by user
    :param op_dict: dictionary with the valid operations
    :return: True or False
    """
    if operation in op_dict.keys():
        return True
    else:
        return False


def realize_operation(num1, num2, operation, op_dict):
    """
    do the expected math between two numbers and the valid operation
    :param num1: int or float
    :param num2: int or float
    :param operation: operation entered by the user
    :param op_dict: dictionary with the valid operations
    :return: int or float
    """
    return op_dict[operation](num1, num2)


calculate = True
operation_dict = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
option = "n"
r = 0

print(logo)
while option != 'q':
    if option == "n":
        num1 = validate_number(input("What is the first num?: "))
        if type(num1) is str:
            print(num1)
            continue
    else:
        num1 = r

    operation = input("pick an operation +, -, *, /: ")
    if not validate_operation(operation, operation_dict):
        print(f"operation {operation} is not valid")
        continue

    num2 = validate_number(input("What is the second num?: "))
    if type(num1) is str:
        print(num2)
        continue

    r = realize_operation(num1, num2, operation, operation_dict)
    print(f"{num1} {operation} {num2} = {r}")

    option = input(f"Type 'y' to continue calculating with {r} or 'n' to start a new calculation or 'q' to quit': ")

