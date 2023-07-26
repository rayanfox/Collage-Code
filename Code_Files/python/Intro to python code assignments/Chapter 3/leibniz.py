# Put your code here
def leibniz_approximation(iterations):
    approximation = 0.0
    sign = 1.0

    for i in range(iterations):
        term = sign / (2 * i + 1)
        approximation += term
        sign *= -1

    return 4 * approximation

# Getting user input for the number of iterations
num_iterations = int(input("Enter the number of iterations: "))

# Calculating the approximation
approximation = leibniz_approximation(num_iterations)

# Displaying the result
print("Approximation of π:", approximation)
