# we can have an if inside another if statement

x = input("Enter a number: ")

if x:
    x = int(x)
    if x > 30:
        print("The number is bigger than 30")
    else:
        if x % 2 == 0:
            print("This is an even number.")
        else:
            print("This is an odd number.")
else:
    print("in this case the user didn't enter a value")
    exit(0)





