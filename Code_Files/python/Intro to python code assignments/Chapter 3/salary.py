# Put your code here
def calculate_salary(starting_salary, annual_increase, num_years):
    salary_schedule = []

    for year in range(1, num_years + 1):
        salary = starting_salary * ((1 + annual_increase / 100) ** (year - 1))
        salary_schedule.append((year, salary))

    return salary_schedule


def print_salary_schedule(salary_schedule):
    print("Year   Salary")
    print("-------------")
    for year, salary in salary_schedule:
        print(f"{year:2d}    {salary:.2f}")


if __name__ == "__main__":
    try:
        starting_salary = float(input("Enter the starting salary: $"))
        annual_increase = float(input("Enter the annual % increase: "))
        num_years = int(input("Enter the number of years: "))

        salary_schedule = calculate_salary(starting_salary, annual_increase, num_years)
        print_salary_schedule(salary_schedule)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
