import math

def guess_number(smaller, larger):
    lower_bound = smaller
    upper_bound = larger
    num_guesses = math.ceil(math.log2(larger - smaller + 1))

    for _ in range(num_guesses):
        guess = (lower_bound + upper_bound) // 2
        print(f"{lower_bound} {upper_bound}")
        print(f"Your number is {guess}")
        response = input("Enter =, <, or >: ")

        if response == "=":
            print(f"Hooray, I've got it in {num_guesses} tries!")
            return
        elif response == "<":
            upper_bound = guess - 1
        elif response == ">":
            lower_bound = guess + 1

    print("I'm out of guesses, and you cheated!")

if __name__ == "__main__":
    try:
        smaller_number = int(input("Enter the smaller number: "))
        larger_number = int(input("Enter the larger number: "))

        guess_number(smaller_number, larger_number)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
