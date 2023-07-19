def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading file.")


def navigate_file():
    filename = input("Enter the filename: ")
    lines = read_file(filename)

    if not lines:
        return

    num_lines = len(lines)
    print("The file has {} lines.".format(num_lines))

    while True:
        line_number = input("Enter a line number (1-{}), or 0 to quit: ".format(num_lines))

        if line_number == '0':
            break

        try:
            line_number = int(line_number)
            if 1 <= line_number <= num_lines:
                print("Line {}: {}".format(line_number, lines[line_number - 1].strip()))
            else:
                print("Invalid line number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid line number or 0 to quit.")


if __name__ == '__main__':
    navigate_file()
