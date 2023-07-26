
def check_equilateral_triangle(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

is_equilateral = check_equilateral_triangle(side1, side2, side3)


if is_equilateral:
    print("The triangle is equilateral. ")
else:
    
    print("The triangle is not equilateral.")
