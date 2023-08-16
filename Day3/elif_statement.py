# el elif works as another condition inside one if_else statement
x = input("Enter a number: ")


x = int(x)
if x >= 70:
    print("The number is bigger or equal than 70")
elif x > 50:
    print("The number is bigger than 50 but is smaller than 70")
else:
    if x % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")