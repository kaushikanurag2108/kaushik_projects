import string


def caesor_cipher(message, shift, encode_decode):
    if encode_decode == 'decode':
        shift *= -1
    decoded_message = ''
    alphabet_lower = list(string.ascii_lowercase)
    for letter in message:
        if letter not in alphabet_lower:
            decoded_message += letter
        else:
            decode_index = alphabet_lower.index(letter)
            decoded_message += alphabet_lower[(decode_index + shift) % len(alphabet_lower)]
    print(decoded_message)


encode_decode = input('Do you want to encode or decode? ').lower()
message = input('Enter your message to be encoded/decoded! ').lower()
shift = int(input('Enter shift digit '))
caesor_cipher(message, shift, encode_decode)
