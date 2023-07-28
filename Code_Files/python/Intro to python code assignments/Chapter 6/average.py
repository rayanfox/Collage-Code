from functools import reduce

def read_numbers_from_file(file_name):
    with open(file_name, 'r') as file:
        numbers = []
        for line in file:
            parts = line.strip().split()
            for part in parts:
                try:
                    number = float(part)
                    numbers.append(number)
                except ValueError:
                    print(f"Warning: Ignoring non-numeric data in the file: '{part}'")
    return numbers

def calculate_sum(numbers):
    return reduce(lambda x, y: x + y, numbers)

def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)

def main():
    file_name = input("Enter the input file name: ")

    try:
        numbers = read_numbers_from_file(file_name)
        if not numbers:
            print("Error: The file is empty or contains no numbers.")
        else:
            average = calculate_average(numbers)
            print("The average is", average)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    main()
