# The spedometer skips the number 5, find out the true mileage

def calculate_true_distance(distance: int) -> int:
    counter: int = 0

    for i in range(distance):
        if not "5" in str(i+1):
            counter += 1
    return counter


result = calculate_true_distance(160648)

print(result)