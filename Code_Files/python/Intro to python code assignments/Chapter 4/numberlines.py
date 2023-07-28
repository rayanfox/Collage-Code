# Put your code here
def number_lines(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        line_number = 1
        for line in input_f:
            output_line = f'{line_number: >4}> {line}'
            output_f.write(output_line)
            line_number += 1


def main():
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    number_lines(input_file, output_file)
    print("Program listing created successfully!")


if __name__ == '__main__':
    main()
