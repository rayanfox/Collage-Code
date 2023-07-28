import math

def newton(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break

    return estimate

def main():
    while True:
        # Receive the input number from the user
        user_input = input("Enter a positive number or enter/return to quit: ")

        # Check if the user wants to quit
        if user_input == "":
            break

        try:
            x = float(user_input)
            if x < 0:
                print("Please enter a positive number.")
            else:
                # Calculate and display the estimates
                program_estimate = newton(x)
                python_estimate = math.sqrt(x)
                print("The program's estimate is", program_estimate)
                print("Python's estimate is", python_estimate)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
