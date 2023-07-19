# Put your code here
from collections import Counter

def display_concordance(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()

        word_counts = Counter(words)

        for word, count in sorted(word_counts.items()):
            print(f"{word} {count}")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading file.")


def main():
    filename = input("Enter the input file name: ")
    display_concordance(filename)


if __name__ == '__main__':
    main()
