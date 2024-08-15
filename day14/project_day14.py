"""
We are going to build a higher or low classic game
"""

from art import logo, vs
from game_data import data
from random import choice


def print_info_from_item(item, prev_item=None):
    """
    :param item: item to check info
    :param prev_item: if there is a previous item the message change to "Against"
    """
    message = "Compare A: {}, a {}, from {}"
    if prev_item:
        message = "Against B: {}, a {}, from {}"
    name = item["name"]
    description = item["description"]
    country = item["country"]
    message = message.format(name, description, country)
    print(message)


def get_item_from_data(data_items, prev_item=None):
    """
    :param data_items: list of dictionaries to get an item
    :param prev_item: previous item got
    :return: a new item different from the previous one if it exists
    """
    new_item = choice(data_items)
    while prev_item == new_item:
        new_item = choice(data_items)
    return new_item


def get_user_option(item_a, item_b):
    """
    :param item_a: item to Compare - first option
    :param item_b: item against the item1 - second option
    :return: the order of which one is the winner according to the user
    """
    while True:
        user_answer = input("Who has more followers? type A or B: ").upper()
        if user_answer not in ['A', 'B']:
            print("Please provide a valid option ")
            continue

        if user_answer == 'A':
            return item_a, item_b
        else:
            return item_b, item_a


def check_result(item_a, item_b, current_score):
    """
    :param item_a: item to Compare - first option
    :param item_b: item against the item1 - second option
    :param current_score: current score in the game
    :return: (item, new_score) if the user is correct or (None, 0) if it is not correct
    """
    user_winner, user_loser = get_user_option(item_a, item_b)
    if user_winner['follower_count'] >= user_loser['follower_count']:
        current_score += 1
        print(f"You are right!! Current Score: {current_score}")
        return user_winner, current_score
    else:
        print("You are wrong!!!")
        return None, 0


print(logo)
score = 0
continue_playing = True
result = None

while continue_playing:
    if score == 0:
        item1 = get_item_from_data(data)
    else:
        item1 = result
    print_info_from_item(item1)
    print(vs)
    item2 = get_item_from_data(data, prev_item=item1)
    print_info_from_item(item2, prev_item=item1)
    result, score = check_result(item1, item2, score)
    if not result or score == 50:
        print("Game finished!")
        break

