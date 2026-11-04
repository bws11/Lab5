numbers = [1, 2, 3, 1]

def contains_duplicates(numbers: list):
    # Sets remove suplicates
    set_numbers = set(numbers)

    if len(set_numbers) == len(numbers):
        return False
    return True


print(f"Contains duplicates: {contains_duplicates(numbers)}")