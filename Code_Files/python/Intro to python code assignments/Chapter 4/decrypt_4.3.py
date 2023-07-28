def decrypt_text(coded_text, distance):
    plain_text = ""
    for ch in coded_text:
        ord_value = ord(ch)
        plain_value = ord_value - distance
        if plain_value < ord('a'):
            plain_value = ord('z') - (distance - (ord_value - ord('a')) - 1)
        plain_text += chr(plain_value)
    return plain_text


def decrypt_file(input_filename, output_filename, distance):
    try:
        with open(input_filename, 'r') as input_file:
            coded_text = input_file.read().strip()

        decrypted_text = decrypt_text(coded_text, distance)

        with open(output_filename, 'w') as output_file:
            output_file.write(decrypted_text)

        print("Decryption successful. Decrypted content written to", output_filename)

    except FileNotFoundError:
        print("Input file not found. Please make sure the filename is correct.")


if __name__ == "__main__":
    input_filename = input("Enter the input file name: ")
    output_filename = input("Enter the output file name: ")
    distance = int(input("Enter the distance value: "))

    decrypt_file(input_filename, output_filename, distance)
