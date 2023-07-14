# Put your code here
kilometer = int(input("Enter the distance: "))

degreesPerMin = 90 * 60
oneKilo = degreesPerMin / 10000

nauticalmile = oneKilo * kilometer

print("The number of nautical miles is " + str(nauticalmile))
