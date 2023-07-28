# Put your code here
def decimal_to_octal(decimal):
    octal = 0
    power = 0

    # Iterate until the decimal number becomes 0
    while decimal > 0:
        # Extract the remainder when the decimal number is divided by 8
        remainder = decimal % 8

        # Multiply the remainder by the corresponding power of 10 and add to the octal value
        octal += remainder * (10 ** power)

        # Update the decimal number and increase the power
        decimal //= 8
        power += 1

    return octal

# Test the function
decimal_number = int(input("Enter a decimal number: "))
octal_number = decimal_to_octal(decimal_number)
print("Octal equivalent:", octal_number)
