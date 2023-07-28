# Put your code here
codedTxt = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainTxt = ("")
for ch in codedTxt:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord(' '):
        cipherValue = ord('~') - \
                (distance - (ord('~') - ordValue - 1))
    plainTxt += chr(cipherValue)
print(plainTxt)
