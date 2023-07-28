
def myRange(*args):
    start = None
    stop = None
    step = None

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError(f"myRange expected at most 3 arguments, got {len(args)}")

    if start is None:
        start = 0

    if step is None:
        step = 1 if start < stop else -1

    result = []
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        result.append(current)
        current += step

    return result

# Test cases
print(myRange(10))          # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10))       # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10, 2))    # Output: [1, 3, 5, 7, 9]
print(myRange(10, 1, -2))   # Output: [10, 8, 6, 4, 2]
