#10-2

#Write a program that allows the user to navigate the lines of text in a file. The program should prompt the user for a filename and input the lines of text into a list. The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.

def read_file(filename):
    
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
   
    filename = input("Enter the filename: ")
    lines = read_file(filename)
    if lines is None:
        return
    num_lines = len(lines)
    while True:
        print(f"There are {num_lines} lines in the file.")
        line_num = input("Enter a line number (0 to quit): ")
        if not line_num.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        line_num = int(line_num)
        if line_num == 0:
            break
        elif line_num < 1 or line_num > num_lines:
            print(f"Invalid line number. Please enter a number between 1 and {num_lines}.")
            continue
        else:
            print(f"Line {line_num}: {lines[line_num-1]}")

if __name__ == "__main__":
     main()

