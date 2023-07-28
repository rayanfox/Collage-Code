import math

# Initialize the tolerance
TOLERANCE = 0.000001

def newton(x, estimate):
    """Returns the square root of x using Newton's method."""
    # Compute the difference and test for the base case
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        # Recurse after improving the estimate
        return newton(x, (estimate + x / estimate) / 2)

def main():
    """Allows the user to obtain square roots using Newton's method."""
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x, 1))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()
