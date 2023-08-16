# the if statements works with boolean values when something is true or not

# important thing to have in mind is that if a variable is not 0 or none or empty object it is true in an if statement

# another important aspect is that not all the code is executed, but it checks all the conditionals in order
# and if it finds that one of the condition is true, it runs the code inside it and forget about the code of the other
# conditionals

x = input("Enter a number: ")

if x:
    print("in this case the number exists")
else:
    print("in this case the user didn't enter a value")
    exit(0)

x = int(x)
if x > 30:
    print("The number is bigger than 30")
else:
    print("The number is less or equal than 30")

if x % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

