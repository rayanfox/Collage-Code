# Put your code here
def print_unique_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()

        unique_words = sorted(set(words), key=lambda x: (x.lower(), x))

        for word in unique_words:
            print(word)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading file.")


def main():
    filename = input("Enter the input file name: ")
    print_unique_words(filename)


if __name__ == '__main__':
    main()
