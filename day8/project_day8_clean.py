"""
Caesar-cipher final version
"""
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(user_text, shift_amount, user_direction):
    msg = ""
    for character in user_text:
        if character not in alphabet:
            msg += character
            continue

        index = alphabet.index(character)
        if user_direction == "encoded":
            if index + shift_amount >= len(alphabet):
                new_index = (index + shift_amount) - len(alphabet)
            else:
                new_index = index + shift_amount
        else:
            new_index = index - shift_amount

        msg += alphabet[new_index]

    print(f"The {direction} message is: {msg}")


print(logo)
use_caesar = "yes"
while use_caesar == "yes":
    direction = input("Type 'encoded' to encrypt, type 'decoded' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >= len(alphabet):
        shift = shift % len(alphabet)
    caesar(user_text=text, shift_amount=shift, user_direction=direction)
    use_caesar = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
print("Goodbye.")