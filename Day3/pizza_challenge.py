
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0

if extra_cheese == "Y":
    price += 1

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price += 25

print(f"Your final bill is: ${price}.")
