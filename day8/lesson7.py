"""
Caesar-cipher part3
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encoded' to encrypt, type 'decoded' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(user_text, shift_amount, user_direction):
    msg = ""
    for letter in user_text:
        index = alphabet.index(letter)
        if user_direction == "encode":
            if index + shift_amount >= len(alphabet):
                new_index = (index + shift_amount) - len(alphabet)
            else:
                new_index = index + shift_amount
        else:
            new_index = index - shift_amount
        msg += alphabet[new_index]

    print(f"The {direction} message is {msg}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(user_text=text, shift_amount=shift, user_direction=direction)
