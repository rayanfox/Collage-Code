def shiftLeft(bits):
    shifted_bits = bits[1:] + bits[0]
    return shifted_bits

bits = input("Enter a string of bits: ")
shifted_left = shiftLeft(bits)
print(shifted_left)
