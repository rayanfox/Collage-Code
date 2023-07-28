# Put your code here
def copy_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file_in:
            content = file_in.read()
        
        with open(output_file, 'w') as file_out:
            file_out.write(content)
        
        print("File copied successfully!")
    except FileNotFoundError:
        print("File not found.")
    except:
        print("An error occurred while copying the file.")

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

copy_file(input_file, output_file)
