def shifted_alphabet(shift, alphabet):
    """
    this function will help us to obtain the new alphabet to encode or decode the message
    :param shift: offset
    :param alphabet: list of letters in regular alphabetic order
    :return: new alphabet to encode or decode the text
    """
    limit = len(alphabet)
    limit_exceeded = shift
    new_alphabet = []

    for pos in range(0, limit):
        if limit > (pos + shift):
            new_alphabet.append(alphabet[pos + shift])
        else:
            new_alphabet.append(alphabet[shift - limit_exceeded])
            limit_exceeded -= 1

    return new_alphabet


def encrypt(text, shift, alphabet):
    """
    This function will help us to encrypt the text using the shift and the regular alphabet

    :param text: message to encode
    :param shift: offset to encode the message
    :param alphabet: list of letters in regular alphabetic order
    :return: encrypted message
    """
    mod_alphabet = shifted_alphabet(shift=shift, alphabet=alphabet)
    encrypted_message = ""
    for letter in text:
        position = alphabet.index(letter)
        encrypted_message += mod_alphabet[position]

    return encrypted_message


def decrypt(text, shift, alphabet):
    """
    This function will help us to decrypt the text using the shift and the regular alphabet

    :param text: message to encode
    :param shift: offset to encode the message
    :param alphabet: list of letters in regular alphabetic order
    :return: decrypted message
    """
    mod_alphabet = shifted_alphabet(shift=shift, alphabet=alphabet)
    decrypted_message = ""
    for letter in text:
        position = mod_alphabet.index(letter)
        decrypted_message += alphabet[position]

    return decrypted_message


def caesar(direction, text, shift):
    """

    :param direction:
    :param text:
    :param shift:
    :return:
    """

    new_message = ""
    if direction == 'encode':
        new_message = encrypt(text=text, shift=shift, alphabet=alphabet)
    elif direction == 'decode':
        new_message = decrypt(text=text, shift=shift, alphabet=alphabet)
    return f"the {direction} message is {new_message}"


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

caesar_again = "yes"
valid_caesar_options = ["encode", "decode"]

while caesar_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction in valid_caesar_options:
        message_to_show = caesar(direction.lower(), text, shift)
        print(message_to_show)
        caesar_again = input('Type "yes" if you like to use the cipher again: ')
    else:
        print(f"{direction} is not a valid option please enter a valid one")
