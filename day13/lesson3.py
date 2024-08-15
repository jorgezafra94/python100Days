"""
Debugging catching an exception
"""

try:
    age = int(input("enter your age: "))
except ValueError as e:
    print(e)
else:
    if age > 18:
        print("you are an adult right now")
