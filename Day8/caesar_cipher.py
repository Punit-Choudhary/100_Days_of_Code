# Caesar Cipher -- Encoder, Decoder

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encoded_text = ""
    for letter in text:
        position = alphabet.index(letter) + shift
        encoded_text += alphabet[position]
    print(f"The encoded text is {encoded_text}")

def decrypt(text, shift):
    decoded_text = ""
    for letter in text:
        position = alphabet.index(letter) - shift
        decoded_text += alphabet[position]
    print(f"The decoded text is {decoded_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)