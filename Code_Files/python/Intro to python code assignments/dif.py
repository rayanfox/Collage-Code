"""
File: dif.py
Project 4.10

Deterines whether or not the contents of two text
files are the same.  Outputs "Yes" if that is the
case or "No" and the first two lines that differ if
that is not the case.
"""

# Put your code here
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print("No")
                print(line1.strip())
                print(line2.strip())
                return
    print("Yes")


def main():
    file1 = input("Enter the first file name: ")
    file2 = input("Enter the second file name: ")
    compare_files(file1, file2)


if __name__ == '__main__':
    main()
