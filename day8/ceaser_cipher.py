alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def main_func():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == str("encode"):
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    else:
        print("Try again.")
        main_func()


def encrypt(text, shift):
    plain_text = text
    cipher_text = ""

    for char in plain_text:
        cipher_text += alphabet[alphabet.index(char) + shift]

    print(f"The encoded text is {cipher_text}.")


def decrypt(text, shift):
    plain_text = text
    cipher_text = ""

    for char in plain_text:
        cipher_text += alphabet[alphabet.index(char) - shift]

    print(f"The encoded text is {cipher_text}.")


main_func()