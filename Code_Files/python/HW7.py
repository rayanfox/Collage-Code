64.#1. The tax calculator program of the case study outputs a floating-point number
#modify the program to display at most two digits of precision in the output
#Number.

tax_r = 0.20
income = float(input("Enter your income: "))
tax = round(income * tax_r, 2)
print(f"Your tax is ${tax:.2f}")

#2. You can calculate the surface area of a cube if you know the length of an edge.
#Write a program that takes the length of an edge (an integer) as input and prints
#the cube’s surface area as output.

edge = int(input("Enter the length of an edge: "))
area = 6 * edge ** 2
print("The surface area of the cube is", area)

#3. Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
#like to buy LP record albums. The store rents new videos for $3.00 a night, and
#oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
#can use to calculate the total charge for a customer’s video rentals. The program
#should prompt the user for the number of each type of video and output the total
#Cost.

new_videos = int(input("number of new videos rented: "))
old_videos = int(input("number of old videos rented: "))

new_price = 3.00
old_price = 2.00

total_cost = (new_videos * new_price) + (old_videos * old_price)

print("Total cost for the rentals is $", total_cost)



#4. Write a program that takes the radius of a sphere (a floating-point number) as
#input and then outputs the sphere’s diameter, circumference, surface area, and
#Volume.

import math

radi = float(input("Enter sphere radius here"))

Diam = 2 * radi
Circumference = 2 * math.pi * radi
Surface = 4 * math.pi * radi ** 2
Vol = (4/3) * math.pi * radi ** 3


#7. Write a program that calculates and prints the number of minutes in a year.

print("Diameter of the sphere is:", Diam)
print("Circumference of the sphere is:", Circumference)
print("Surface area of the sphere is:", Surface)
print("Volume of the sphere is:", Vol)

Minutes_Per_hour =  60
Hours_Per_day = 24
Days_Per_year = 365
Total_Minutes = Minutes_Per_hour * Hours_Per_day * Days_Per_year

print("the number of total minutes in a year is", Total_Minutes ) 


#10. An employee’s total weekly pay equals the hourly wage multiplied by the total
#number of regular hours plus any overtime pay. Overtime pay equals the total
#overtime hours multiplied by 1.5 times the hourly wage. Write a program that
#takes as inputs the hourly wage, total regular hours, and total overtime hours and
#displays an employee’s total weekly pay


hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the total regular hours worked: "))
overtime_hours = float(input("Enter the total overtime hours worked: "))

regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * hourly_wage * 1.5
total_pay = regular_pay + overtime_pay


print("The employee's total weekly pay is:", total_pay)