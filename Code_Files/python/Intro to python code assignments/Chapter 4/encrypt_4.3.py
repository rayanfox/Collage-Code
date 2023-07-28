def encrypt_text(plain_text, distance):
    code = ""
    for ch in plain_text:
        ord_value = ord(ch)
        cipher_value = ord_value + distance
        if cipher_value > ord('z'):
            cipher_value = ord('a') + distance - (ord('z') - ord_value + 1)
        code += chr(cipher_value)
    return code


def encrypt_file(input_filename, output_filename, distance):
    try:
        with open(input_filename, 'r') as input_file:
            plain_text = input_file.read().strip()

        encrypted_text = encrypt_text(plain_text, distance)

        with open(output_filename, 'w') as output_file:
            output_file.write(encrypted_text)

        print("Encryption successful. Encrypted content written to", output_filename)

    except FileNotFoundError:
        print("Input file not found. Please make sure the filename is correct.")


if __name__ == "__main__":
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")
    distance = int(input("Enter the distance value: "))

    encrypt_file(input_filename, output_filename, distance)
