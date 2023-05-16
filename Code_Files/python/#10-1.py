#hw-10

# A group of statisticians at a local college has asked you to create a set of functions that compute the median and mode of a set of numbers, as defined in Section 5.4. Define these functions in a module named stats.py. Also include a function named mean , which computes the average of a set of numbers. Each function should expect a list of numbers as an argument and return a single number. Each function should return 0 if the list is empty. Include a main function that tests the three statistical functions with a given list.


def median(numbers):
 
    n = len(numbers)
    if n == 0:
        return 0
    sorted_nums = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):

    if len(numbers) == 0:
        return 0
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    mode_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == mode_count]
    if len(modes) == len(numbers):
        return 0
    return modes[0]

def mean(numbers):
 
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def main():

    nums = [1, 2, 2, 3, 4, 5]
    print("List of numbers:", nums)
    print("Median:", median(nums))
    print("Mode:", mode(nums))
    print("Mean:", mean(nums))

if __name__ == "__main__":
    main()




