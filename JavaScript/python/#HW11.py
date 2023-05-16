#HW11

#Package Newton’s method for approximating square roots (Case Study 3.6) in a function named newton . This function expects the input number as an argument and returns the estimate of its square root. The script should also include a main function that allows the user to compute square roots of inputs until she presses the enter/return key.

def newton(n):
   
    x = n / 2  # initial guess
    while True:
        y = (x + n / x) / 2  # improved estimate
        if abs(y - x) < 0.0001:  # check for convergence
            return y
        x = y  # update estimate

def main():

    while True:
        try:
            n = input("Enter a number to compute its square root (or press Enter to quit): ")
            if not n:
                break  # exit if user presses Enter
            n = float(n)
            if n < 0:
                raise ValueError("Cannot compute square root of a negative number")
            print("The square root of {} is {:.4f}".format(n, newton(n)))
        except ValueError as e:
            print(e)

if __name__ == '__main__':


#A list is sorted in ascending order if it is empty or each item except the last one is less than or equal to its successor. Define a predicate isSorted that expects a list as an argument and returns True if the list is sorted, or returns False otherwise. (Hint: For a list of length 2 or greater, loop through the list and compare pairs of items, from left to right, and return False if the first item in a pair is greater.)

    def isSorted(lst):
   
        if len(lst) < 2:  # empty or singleton list is always sorted
            return True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:  # found a pair of items out of order
                return False
        return True
#add a command to this chapter’s case study program that allows the user to view the contents of a file in the current working directory. When the command is selected, the program should display a list of filenames and a prompt for the name of the file to be viewed. Be sure to include error recovery.

import os

def print_menu():
    
    print("Menu:")
    print("1. Compute sum")
    print("2. Compute factorial")
    print("3. Compute fibonacci sequence")
    print("4. View file contents")
    print("5. Quit")

def compute_sum():
   
    lst = input("Enter a list of numbers, separated by spaces: ").split()
    lst = [float(x) for x in lst]  # convert each string to a float
    print("The sum is:", sum(lst))

def compute_factorial():
   
    n = int(input("Enter a nonnegative integer: "))
    if n < 0:
        print("Error: Input must be nonnegative")
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        print("{}! = {}".format(n, result))

def compute_fibonacci():
    
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Error: Input must be positive")
    else:
        a, b = 0, 1
        print("Fibonacci sequence:")
        for i in range(n):
            print(a, end=' ')
            a, b = b, a+b
        print()

def view_file_contents():
   
    files = os.listdir('.')
    print("Files in the current directory:", ', '.join(files))
    while True:
        filename = input("Enter the name of a file to view (or press Enter to quit): ")
        if not filename:
            break
        try:
            with open(filename, 'r') as f:
                contents = f.read()
            print("Contents of {}:\n{}".format(filename, contents))
        except FileNotFoundError:
            print("Error: File not found")
        except PermissionError:
            print("Error: Permission denied")
        except Exception as e:
            print("Error:", e)

def main():

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            compute_sum()
        elif choice == '2':
            compute_factorial()
        elif choice == '3':
            compute_fibonacci()
        elif choice == '4':
            view_file_contents()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice")

if __name__ == '__main__':
    main()

#write a program that computes and prints the average of the numbers in a text file. You should make use of two higher-order functions to simplify the design.

def read_numbers(filename):
    
    with open(filename, 'r') as f:
        numbers = [float(line.strip()) for line in f]
    return numbers

def compute_average(numbers):
    
    if len(numbers) == 0:
        return None
    else:
        return sum(numbers) / len(numbers)

def main():

    filename = input("Enter the name of the file containing the numbers: ")
    numbers = read_numbers(filename)
    average = compute_average(numbers)
    if average is None:
        print("The file is empty.")
    else:
        print("The average of the numbers is:", average)

if __name__ == '__main__':
    main()

#you may make an application in tkinter that asks the user for the number of calories eaten at breakfast, lunch and dinner. Recommended daily calorie intakes in the US are around 2,500 for men and 2,000 for women. To lose 1 pound, or 0.5kg per week, you will need to cut 500 calories from your daily menu. Have your app report on the user's weight loss.

import tkinter as tk


DAILY_CALORIES_MEN = 2500
DAILY_CALORIES_WOMEN = 2000

class CalorieTracker:
    def __init__(self, master):
        self.master = master
        master.title("Calorie Tracker")

        self.calories = {"breakfast": 0, "lunch": 0, "dinner": 0}

        self.create_widgets()

    def create_widgets(self):
      
        self.breakfast_label = tk.Label(self.master, text="Breakfast Calories:")
        self.breakfast_label.pack()
        self.breakfast_entry = tk.Entry(self.master)
        self.breakfast_entry.pack()

      
        self.lunch_label = tk.Label(self.master, text="Lunch Calories:")
        self.lunch_label.pack()
        self.lunch_entry = tk.Entry(self.master)
        self.lunch_entry.pack()

       
        self.dinner_label = tk.Label(self.master, text="Dinner Calories:")
        self.dinner_label.pack()
        self.dinner_entry = tk.Entry(self.master)
        self.dinner_entry.pack()

       
        self.submit_button = tk.Button(self.master, text="Submit", command=self.calculate_calories)
        self.submit_button.pack()

       
        self.output_label = tk.Label(self.master, text="")
        self.output_label.pack()

    def calculate_calories(self):
        
        breakfast_calories = float(self.breakfast_entry.get())
        lunch_calories = float(self.lunch_entry.get())
        dinner_calories = float(self.dinner_entry.get())

     
        total_calories = breakfast_calories + lunch_calories + dinner_calories

       
        gender = input("Enter your gender (M/F): ")
        if gender.lower() == "m":
            recommended_calories = DAILY_CALORIES_MEN
        elif gender.lower() == "f":
            recommended_calories = DAILY_CALORIES_WOMEN
        else:
            self.output_label.config(text="Invalid gender.")
            return

        weight_loss = (total_calories - recommended_calories) / 500.0

       
        self.output_label.config(text="You will lose {:.1f} pounds this week.".format(weight_loss))

root = tk.Tk()
app = CalorieTracker(root)
root.mainloop()

