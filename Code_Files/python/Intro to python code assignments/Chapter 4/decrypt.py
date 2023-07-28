# Put your code here

def caesar_decipher(encrypted_text, distance):
    plaintext = ""
    for char in encrypted_text:
        if char.isprintable():
            ascii_val = ord(char)
            decrypted_val = (ascii_val - distance) % 256
            decrypted_char = chr(decrypted_val)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


encrypted_text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))


plaintext = caesar_decipher(encrypted_text, distance)


print("Plaintext:", plaintext)
