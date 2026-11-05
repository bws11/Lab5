# two sum

def two_sum(numbers: list, target: int) -> list:
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if numbers[i] + numbers[j] == target:
                    return [numbers[i], numbers[j]]

    # not possible
    return []



answer = two_sum(
    [2, 5, 3, 2, 6],
    9
)

print(answer)