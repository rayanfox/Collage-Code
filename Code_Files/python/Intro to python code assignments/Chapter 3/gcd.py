def euclidean_algorithm(a, b):
    while b != 0:
        print(f"{a} divided by {b}, remainder = {a % b}")
        a, b = b, a % b

    return a

def main():
    try:
        smaller_num = int(input("Enter the smaller number: "))
        larger_num = int(input("Enter the larger number: "))

        if smaller_num < 0 or larger_num < 0:
            raise ValueError("Please enter positive integers.")

        print("\nSteps to find the GCD using Euclidean algorithm:")
        if smaller_num > larger_num:
            smaller_num, larger_num = larger_num, smaller_num
        elif smaller_num == 0:
            print("\nThe greatest common divisor is", larger_num)
            return

        gcd = euclidean_algorithm(larger_num, smaller_num)
        print("\nThe greatest common divisor is", gcd)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

