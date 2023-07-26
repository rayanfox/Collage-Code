initial_height = float(input("Enter the height from which the ball is dropped: "))
bounciness_index = float(input("Enter the bounciness index of the ball: "))
num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

# Calculate and print the total distance
total_distance = initial_height
for _ in range(num_bounces):
    bounce_height = bounciness_index * total_distance
    total_distance += 2 * bounce_height

rounded_distance = round(total_distance, 3)
print("Total distance traveled is: {} units.".format(rounded_distance))
