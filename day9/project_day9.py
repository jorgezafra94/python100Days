"""
Blind auction program
"""
from replit import clear
from art import logo


# HINT: You can call clear() to clear the output in the console.

def get_winner(info):
    higher_amount = 0
    winner = ""
    for user in info:
        name, bid = user["name"], user["bid"]
        if bid > higher_amount:
            higher_amount = bid
            winner = name
    print(f"The winner is {winner} with a bid of ${higher_amount}")


print(logo)
print("Welcome to the secret auction program.")
auction_info = []
auction_alive = "yes"

while auction_alive == "yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid? :$"))
    user = {"name": name, "bid": bid}
    auction_info.append(user)
    auction_alive = input("Are there any other bidders? type 'yes' or 'no': ").lower()
    if auction_alive == "yes":
        clear()

print("Bid close ...")
get_winner(auction_info)
