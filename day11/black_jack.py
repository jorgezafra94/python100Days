"""
Here we are going to create the functions of a blackjack game
"""
import random


def total_hand(list_of_cards: list):
    """
    this function will return the sum of cards in the hand
    :param list_of_cards: list of cards
    :return: sum of card values
    """
    total = 0
    tens = ['J', 'Q', 'K']

    # make A in the last position
    if 'A' in list_of_cards:
        list_of_cards.remove('A')
        list_of_cards.append('A')

    for elem in list_of_cards:
        if elem in tens:
            total += 10
        elif elem == 'A':
            if total > 11:
                total += 1
            else:
                total += 11
        else:
            total += elem

    return total


def player_game(player_hand: list, set_cards: list):
    """
    this function add carts and check if the player lose
    :param player_hand: cards on the player hands
    :param set_cards: cards of the game
    :return: score
    """
    score = total_hand(player_hand)
    while score <= 21:
        more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        if more_cards == 'y':
            new_card = random.choice(set_cards)
            player_hand.append(new_card)
            score = total_hand(player_hand)
            print(f"Your cards are: {player_hand} and your current score is {score}")
        else:
            break
    return score


def dealer_game(dealer_hand: list, set_cards: list):
    """
    this function add carts and check if the dealer lose
    :param dealer_hand: cards on the dealer hands
    :param set_cards: cards of the game
    :return: score
    """
    score = total_hand(dealer_hand)
    while score < 17:
        new_card = random.choice(set_cards)
        dealer_hand.append(new_card)
        score = total_hand(dealer_hand)
    return score


def check_if_dealer_has_to_play(player_score):
    """
    check if the player won or lose already with only his/her hand
    :param player_score: score
    :return: true or false
    """
    if player_score > 21:
        print("YOU LOSE!!!")
    elif player_score == 21:
        print("YOU WON!!!")
    else:
        return True
    return False


def check_winner(player_score, dealer_score):
    """
    check who won
    :param player_score: player total
    :param dealer_score: dealer total
    :return: none
    """

    if dealer_score > 21:
        print("YOU WON!!!!")
    elif player_score == dealer_score:
        print("DRAW!!!")
    elif dealer_score > player_score:
        print("YOU LOSE!!!")
    else:
        print("YOU WON!!!")
