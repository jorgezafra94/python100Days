"""
Write a program that adds the digits in a 2 digit number. e.g.
if the input was 35, then the output should be 3 + 5 = 8
"""

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

addition = first_digit + second_digit
print(f"the result is: {addition}")


