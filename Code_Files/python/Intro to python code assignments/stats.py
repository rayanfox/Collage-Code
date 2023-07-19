def median(numbers):
    if not numbers:
        return 0

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle_index = length // 2

    if length % 2 == 0:
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        return sorted_numbers[middle_index]


def mode(numbers):
    if not numbers:
        return 0

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())
    mode_values = [num for num, count in counts.items() if count == max_count]

    if len(mode_values) == len(numbers):
        return 0

    return mode_values[0]  # Return the first mode value


def mean(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def main():
    lyst = [3, 1, 7, 1, 4, 10]

    print("Median:", median(lyst))
    print("Mode:", mode(lyst))
    print("Mean:", mean(lyst))


if __name__ == '__main__':
    main()
