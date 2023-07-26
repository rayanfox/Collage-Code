# Put your code here:
def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()  # Sort the sides in ascending order

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Get the lengths of the triangle sides from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if is_right_triangle(side1, side2, side3):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
