# Caesar Cipher -- Encoder, Decoder

import art

logo = art.logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    output = ""

    if shift > 26:
        shift %= 26

    if direction == "decode":
            shift *= -1
            
    for letter in text:
        if letter not in alphabet:
            output += letter
        else:
            position = alphabet.index(letter)
            position += shift
            output += alphabet[position]
    print(f"The {direction}d text is {output}")

close = False

while not close:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        caesar(direction, text, shift)
    else:
        print("Wrong Input!")

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    
    if choice == "no":
        close = True