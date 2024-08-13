"""
this project is
the number guessing game
"""

import random


def check_number(winner_num, user_num):
    if winner_num == user_num:
        print("That is right!! that is the winner number")
        return True

    if user_num > winner_num:
        print("Too high")
    else:
        print("Too low")
    return False


def guessing_number(max_num_guesses, winner_num):
    count = max_num_guesses
    for i in range(max_num_guesses):
        print(f"You have {count} attempts to guess the number")
        user_guess = int(input("Make a guess: "))
        count -= 1
        if check_number(winner_num, user_guess):
            break
    else:
        print(f"You lose!!! the number was {winner_num}")


play_again = True
while play_again:
    print("Welcome to the number guessing game!!!!")
    print("Guess the number between 1 and 100")
    rand_number = random.randint(1, 100)
    level = input("select the level of difficulty type 'e' for easy or 'h' for hard: ")
    if level == 'h':
        guessing_number(5, rand_number)
    else:
        guessing_number(10, rand_number)
    again = input("Would you like to play again?? type 'y' or 'n': ")
    if again == 'n':
        play_again = False
