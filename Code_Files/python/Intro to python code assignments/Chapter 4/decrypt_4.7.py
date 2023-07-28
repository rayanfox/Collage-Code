# Put your code here
def decrypt(coded_text):
    decrypted_chars = []
    
    # Split the coded text by space to separate the bit strings
    coded_bits = coded_text.split()
    
    for coded_bits in coded_bits:
        # Step 1: Shift bits one place to the right
        shifted_bits = coded_bits[-1] + coded_bits[:-1]
        
        # Step 2: Convert bit string back to decimal ASCII value
        shifted_ascii = int(shifted_bits, 2)
        
        # Step 3: Subtract 1 from the ASCII value
        decrypted_ascii = shifted_ascii - 1
        
        # Convert the ASCII value to the corresponding character
        decrypted_char = chr(decrypted_ascii)
        
        decrypted_chars.append(decrypted_char)
    
    decrypted_message = ''.join(decrypted_chars)
    return decrypted_message

coded_text = input("Enter the coded text: ")
decrypted_message = decrypt(coded_text)
print(decrypted_message)
