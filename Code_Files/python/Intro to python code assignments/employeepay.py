#Request inputs

Wage = float(input("Enter the wage: $"))
regularHours = float(input("Enter the regular hours: "))
overtimeHours = float(input("Enter the overtime hours: "))
print("")

#Calculate pay

overtime_pay = overtimeHours * Wage * 1.5
totalWeekPay = Wage * regularHours + overtime_pay

#Display pay

print("The total weekly pay is $" + str(totalWeekPay))
