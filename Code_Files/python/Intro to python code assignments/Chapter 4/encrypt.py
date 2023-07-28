# Put your code here
def caesar_cipher(plaintext, distance):
    encrypted_text = ""
    for char in plaintext:
        if char.isprintable():
            ascii_val = ord(char)
            encrypted_val = (ascii_val + distance) % 256
            encrypted_char = chr(encrypted_val)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Input plaintext and distance from the user
plaintext = input("Enter the plaintext: ")
distance = int(input("Enter the distance value: "))

# Encrypt the plaintext using the Caesar cipher
encrypted_text = caesar_cipher(plaintext, distance)

# Output the encrypted text
print("Encrypted text:", encrypted_text)
