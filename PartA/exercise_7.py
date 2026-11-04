list_1 = [1, 2, 45]
list_2 = [3, 5, 5]

def max_difference(list_1: list, list_2: list):
    # find smallest and largest in both lists
    smallest_1 = 1000000000
    largest_1 = -1
    
    for num in list_1:
        if num > largest_1:
            largest_1 = num
        
        if num < smallest_1:
            smallest_1 = num

    # list 2
    smallest_2 = 10000000000
    largest_2 = -1

    for num in list_2:
        if num > largest_2:
            largest_2 = num

        if num < smallest_2:
            smallest_2 = num

    # find the biggest difference
    difference_1 = largest_1 - smallest_2
    difference_2 = largest_2 - smallest_1

    if difference_1 > difference_2:
        return difference_1
    return difference_2


print(max_difference(list_1, list_2))