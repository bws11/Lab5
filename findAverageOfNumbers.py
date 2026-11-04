numbers = (84, 66, 48, 39, 13, 34, 99, 28, 48,
           43, 25, 28, 74, 66, 73, 61, 8, 48,
           68, 84, 48, 8, 30, 28, 37, 22, 40, 91,
           60, 14, 88, 92, 74, 63, 48, 18, 57, 33,
           90, 82, 95, 62, 91, 24, 35, 18, 41, 41,
           36, 19)


total = 0
for number in numbers:
    total += number

average = total / len(numbers)
print(f"The average is {average}")