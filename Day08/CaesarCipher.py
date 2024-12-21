from CaesarCipher_art import logo
import os 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caeser(start_text, shift_amount, cipher_direction):
    if cipher_direction == "decode":
        shift_amount *= -1
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + (shift_amount%26)
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

end = False

while not end:
    os.system('cls')
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    run = input("Type 'yes' to continue, Otherwise type 'no'.\n")
    if run == "no":
        end = True
        print("Goodbye")
    
