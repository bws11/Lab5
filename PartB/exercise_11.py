# longest consecutive sequence

def longest_consecutive_sequence(numbers: list) -> int:
    counter: int = 0
    temp_counter: int = 0
    
    for i in range(1, len(numbers)):
        if numbers[i - 1] + 1 == numbers[i]:
            temp_counter += 1
            if temp_counter > counter:
                counter = temp_counter
        else:
            temp_counter = 0

    return counter + 1


result = longest_consecutive_sequence([1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15])

print(result)