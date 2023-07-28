# Put your code here
def octal_to_decimal(octal):
    decimal = 0
    power = 0

    # Iterate through each digit of the octal number
    while octal > 0:
        # Extract the last digit
        last_digit = octal % 10

        # Multiply the digit by the corresponding power of 8 and add to the decimal value
        decimal += last_digit * (8 ** power)

        # Update the octal number and increase the power
        octal //= 10
        power += 1

    return decimal

# Test the function
octal_number = int(input("Enter an octal number: "))
decimal_number = octal_to_decimal(octal_number)
print("Decimal equivalent:", decimal_number)
