"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1
"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
small, medium, large = 15, 20, 25
pepperoni_small, pepperoni, cheese = 2, 3, 1
total = 0

if size == 'S':
    total += small
    if add_pepperoni == 'Y':
        total += pepperoni_small
else:
    if add_pepperoni == 'Y':
        total += pepperoni
    if size == 'M':
        total += medium
    else:
        total += large

if extra_cheese == 'Y':
    total += cheese

print(f"Your final bill is: ${total}.")


