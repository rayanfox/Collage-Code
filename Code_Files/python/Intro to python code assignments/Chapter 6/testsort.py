def isSorted(lyst):
    """Check if the list is sorted in ascending order."""
    if len(lyst) <= 1:
        return True

    for i in range(len(lyst) - 1):
        if lyst[i] > lyst[i + 1]:
            return False

    return True

def main():
    lyst = []
    print(isSorted(lyst))   # Output: True

    lyst = [1]
    print(isSorted(lyst))   # Output: True

    lyst = list(range(10))
    print(isSorted(lyst))   # Output: True

    lyst[9] = 3
    print(isSorted(lyst))   # Output: False

if __name__ == "__main__":
    main()
