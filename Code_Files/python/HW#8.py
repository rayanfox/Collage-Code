#Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle.
#Recall from the Pythagorean theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1**2 == side2**2 + side3**2 or side2**2 == side1**2 + side3**2 or side3**2 == side1**2 + side2**2:
    print("this is triangle")
else:
    print("this is not triangle")


# A standard science experiment is to drop a ball and see how high it bounces. Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index. For example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6, and the total distance traveled by the ball is 16 feet after one bounce. If the ball were to continue bouncing, the distance after two bounces would be 10 ft 6 111 ft 6 ft 3.6 ft 5 25.6 ft. Note that the distance traveled for each successive bounce is the distance to the floor plus 0.6 of that distance as the ball comes back up. Write a program that lets the user enter the initial height from which the ball is dropped and the number of times the ball is allowed to continue bouncing. Output should be the total distance traveled by the ball.


n_Hight = float(input("Whats the starting hight? "))
number_bounce = int(input("How many times should the ball bounce?  "))
bounciness_amount = float(input("how much should the ball bounce? "))

ball_travel = n_Hight

for i in range(number_bounce):
    ball_travel += n_Hight * bounciness_amount * 2
    n_Hight *= bounciness_amount

print("The ball traveled:", ball_travel)



#Teachers in most school districts are paid on a schedule that provides a salary based on their number of years of teaching experience. For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year. For each year of experience after this first year, up to 10 years, the teacher receives a 2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are the starting salary, the percentage increase, and the number of years in the schedule. Each row in the schedule should contain the year number and the salary for that year.

base_salary = int(input("What is your base salary? "))
percent_increase = float(input("Enter the percent increse (decimals ONLY!)"))
Number_Years = int(input("number of years in schedule: "))

print("years\tsalary")
print("-----\t-----")

salary = base_salary

salary = base_salary
for year in range(1, Number_Years+1):
    print(year, "\t", salary)
    salary += salary * percent_increase / 100


#Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs. After the user presses the enter key, the program should print the sum of the numbers and their average

num = []

while True:
    num = input("put your numbers here( or press the enter key to finish. )")
    if  num == "":
        break
num.append(float(num))
if len(num) > 0:

    sum_of_num = sum(num)
    avg_of_num = sum_of_num / len(num)
    print("the sum of the numbers is: ", sum_of_num)
    print("the avarage of the number is: ", avg_of_num)

else:
    print("nothing supplied")