"""
Caesar-cipher final
"""
# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"
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


# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

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