# Put your code here
# Getting user inputs
initial_population = int(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the rate of growth [a real number > 1]: "))
hours_to_achieve_rate = int(input("Enter the number of hours to achieve the rate of growth: "))
total_growth_hours = int(input("Enter the total hours of growth: "))

# Predict and print the total population
population = initial_population * (growth_rate ** (total_growth_hours // hours_to_achieve_rate))
print("The total population is", population)
