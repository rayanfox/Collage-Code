def repToDecimal(number, base):
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    decimal = 0
    power = len(number) - 1

    for digit in number:
        digit = digit.upper()
        decimal += digits[digit] * (base ** power)
        power -= 1

    return decimal


def main():
    print(repToDecimal('10', 10))  # Decimal: 10
    print(repToDecimal('10', 8))   # Octal: 8
    print(repToDecimal('10', 2))   # Binary: 2
    print(repToDecimal('10', 16))  # Hexadecimal: 16


if __name__ == '__main__':
    main()
