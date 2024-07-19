"""
Password Generator
"""

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_num_char = nr_numbers + nr_symbols + nr_letters
options = [[nr_letters, letters], [nr_symbols, symbols], [nr_numbers, numbers]]
password = ""

for i in range(0, total_num_char):
    rand_option = random.randint(0, len(options) - 1)
    while options[rand_option][0] == 0:
        options.pop(rand_option)
        rand_option = random.randint(0, len(options) - 1)

    option = options[rand_option]
    option_num = option[0]
    option_chars = option[1]
    rand_position = random.randint(0, len(option_chars) - 1)
    password += option_chars[rand_position]
    option[0] = option_num - 1

print(password)
