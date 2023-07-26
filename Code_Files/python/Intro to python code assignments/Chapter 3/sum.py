theSum = 0.0
count = 0

while True:
    data = input("Enter a number or press Enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number
    count += 1

if count > 0:
    average = theSum / count
    print("The sum is", theSum)
    print("The average is", average)
else:
    print("No numbers were entered.")
