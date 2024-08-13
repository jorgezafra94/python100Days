"""
this day is going to be a challenge where we are going to use everything that we learned

Today we are going to build a 21 blackjack
"""

from art import logo
from black_jack import total_hand, player_game, dealer_game, check_winner, check_if_dealer_has_to_play
import random

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

print(logo)
player_cards = random.choices(cards, k=2)
dealer_cards = random.choices(cards, k=2)
player_score = total_hand(player_cards)
print(f"Your cards are: {player_cards} and your current score is {player_score}")
print(f"first card of dealer: {dealer_cards[0]}")
player_score = player_game(player_cards, cards)
print()

if check_if_dealer_has_to_play(player_score):
    dealer_score = total_hand(dealer_cards)
    print(f"Dealer cards are: {dealer_cards} and dealer current score is {dealer_score}")
    dealer_score = dealer_game(dealer_cards, cards)
    check_winner(player_score, dealer_score)

print()
dealer_score = total_hand(dealer_cards)
print(f"Your cards were: {player_cards} and your score was {player_score}")
print(f"Dealer cards were: {dealer_cards} and dealer score was {dealer_score}")
