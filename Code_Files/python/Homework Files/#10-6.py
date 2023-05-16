#10-6

#Define a function decimalToRep that returns the representation of an integer in a given base. The two arguments should be the integer and the base. The function should return a string. It should use a lookup table that associates integers with digits. Include a main function that tests the conversion function with numbers in several bases.

def decimalToRep(num, base):

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if num == 0:
        return '0'
    if num < 0:
        sign = '-'
        num = -num
    else:
        sign = ''

    rep = ''
    while num > 0:
        digit = num % base
        rep = digits[digit] + rep
        num //= base

    return sign + rep

def main():
   
    print(decimalToRep(42, 2))   
    print(decimalToRep(42, 8))   
    print(decimalToRep(42, 16))  
    print(decimalToRep(255, 16)) 
    print(decimalToRep(0, 16))    
    print(decimalToRep(-42, 2)) 

if __name__ == '__main__':
    main()
