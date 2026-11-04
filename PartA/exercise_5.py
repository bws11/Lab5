numbers = [3, 1, 5, 3, 2, 1]

def unique_sorted(numbers: list):
    # Remove duplicates and sort
    numbers = list(set(numbers))
    return numbers[::-1]

print(unique_sorted(numbers))