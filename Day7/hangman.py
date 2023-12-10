"""
Hangman - game
"""

import random
import os
from hangman_words import word_list
from hangman_art import logo, stages


def fill_spaces(letter, expected_word, current_word_list):
    """
    this function is to fill spaces with the guessed letters

    :letter: it is the guessed letter for the user
    :expected_word: random word chosen by the game
    :current_word_list: is the blank word list that we show to the user
    """

    for position in range(0, len(expected_word)):
        if expected_word[position] == letter:
            current_word_list[position] = letter


def check_user_win(letter, expected_word, current_word_list):
    """
    this function is check if the user won the game

    :letter: it is the guessed letter for the user
    :expected_word: random word chosen by the game
    :current_word_list: is the blank word list that we show to the user
    :return: tuple of end_game, result
    """
    fill_spaces(letter, expected_word, current_word_list)
    if "_" not in current_word_list:
        return True, "You Win."
    return False, ""


def check_user_lose(max_lives, number_wrongs, stages):
    """
    this function is to fill spaces with the guessed letters
    :current_lives: it is the current life of the user
    :stages: it is the stage where the user currently is

    :return:
    """
    max_lives -= number_wrongs
    if max_lives > 0:
        return False, stages[max_lives], ""
    return True, stages[max_lives], "You lose, better luck next time."


# first we need to get a random word
possible_words = word_list
stages = stages
logo = logo

# with the next line we can pick out randomly one word
random_word = random.choice(possible_words)

# creating a blank list to fulfill the letters, and it has to have the same length as the random_word
display_word_list = ["_"] * len(random_word)
display_word = "".join(display_word_list)

# counter of hangman, number of total fail guesses that the user can make
lives = len(stages) - 1

used_letters = []
num_wrongs = 0
current_stage = stages[-1]
result = ''
end_game = False

print(logo)
print(current_stage)
print("Wrong letters: ", ", ".join(used_letters))
print(display_word)

while not end_game:
    # now we have to ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    if guess in random_word:
        end_game, result = check_user_win(guess, random_word, display_word_list)
        display_word = "".join(display_word_list)

    else:
        used_letters.append(guess)
        num_wrongs += 1
        end_game, current_stage, result = check_user_lose(lives, num_wrongs, stages)
        if end_game:
            result += f" The winning word was {random_word}"
    print(current_stage)
    print("Wrong letters: ", ", ".join(used_letters))
    print(display_word)


print("************************* ---" + result + "--- ********************************")

