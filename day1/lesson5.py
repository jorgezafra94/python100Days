"""
input built-in function

input function allows us to receive information from the user
Everything we will receive is going to be considered a string

We can have input with prompt or without it

If we want to get number we will have to cast the result to int
"""

result = input("What is your name? ")
print(result)

result2 = input()
print(result)

number = int(input("What is your age? "))
print(number, type(number))
