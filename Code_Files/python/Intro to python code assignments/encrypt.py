# Put your code here
def encrypt(message):
    encrypted_bits = []
    
    for char in message:
        # Step 1: Add 1 to the ASCII value
        shifted_ascii = ord(char) + 1
        
        # Step 2: Convert to bit string
        bit_string = bin(shifted_ascii)[2:]
        
        # Step 3: Shift bits one place to the left
        shifted_bits = bit_string[1:] + bit_string[0]
        
        encrypted_bits.append(shifted_bits)
    
    encrypted_message = ' '.join(encrypted_bits)
    return encrypted_message

message = input("Enter a message: ")
encrypted_message = encrypt(message)
print(encrypted_message)
