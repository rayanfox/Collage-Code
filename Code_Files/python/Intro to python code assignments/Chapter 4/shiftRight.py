def shiftRight(bits):
    shifted_bits = bits[-1] + bits[:-1]
    return shifted_bits

bits = input("Enter a string of bits: ")
shifted_right = shiftRight(bits)
print(shifted_right)
