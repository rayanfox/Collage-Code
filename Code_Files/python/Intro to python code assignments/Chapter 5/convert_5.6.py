def decimalToRep(number, base):
    digits = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    if number == 0:
        return '0'

    rep = ""
    while number > 0:
        digit = number % base
        rep = digits[digit] + rep
        number //= base

    return rep


def main():
    print(decimalToRep(10, 10))  # Decimal: 10
    print(decimalToRep(10, 8))   # Octal: 12
    print(decimalToRep(10, 2))   # Binary: 1010
    print(decimalToRep(10, 16))  # Hexadecimal: A


if __name__ == '__main__':
    main()
