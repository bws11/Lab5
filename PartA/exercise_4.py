temperatures = [12, 15, 18, 21, 19, 16, 14, 11]

def calculate_average(temps: list):
    return sum(temperatures) / len(temperatures)

def find_heighest(temps: list):
    heighest = -1
    for temp in temps:
        if temp > heighest:
            heighest = temp

    return heighest

def find_lowest(temps: list):
    lowest = 100000
    for temp in temps:
        if temp < lowest:
            lowest = temp

    return lowest


# Hot day is above 20 degrees
def count_hot_days(temps: list):
    count = 0
    for temp in temps:
        if temp > 20:
            count += 1

    return count


print(f"The average temp is: {calculate_average(temperatures)}\nThe heighest temp is: {find_heighest(temperatures)}\nThe lowest temp is: {find_lowest(temperatures)}\nThe number of hot days are: {count_hot_days(temperatures)}")