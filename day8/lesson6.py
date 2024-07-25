"""
Caesar-cipher part2
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    caesar_msg = ""
    for letter in plain_text:
        index = alphabet.index(letter)
        if index + shift_amount >= len(alphabet):
            new_index = (index + shift_amount) - len(alphabet)
        else:
            new_index = index + shift_amount
        caesar_msg += alphabet[new_index]

    print(caesar_msg)


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the
#  shift amount and print the decrypted text.

def decrypt(caesar_text, shift_amount):
    original_msg = ""
    for letter in caesar_text:
        index = alphabet.index(letter)
        new_index = index - shift_amount
        original_msg += alphabet[new_index]

    print(original_msg)


# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#  Then call the correct function based on that 'direction' variable. You should be able to test the code to
#  encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(caesar_text=text, shift_amount=shift)
