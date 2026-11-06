# create a pyramid out of stars, based on user input
import random

def create_pyramid(rows: int):
    if rows <= 1:
        return False
    
    rows -= 1
    spaces = rows
    stars = 1

    for i in range(rows):
        if i == 0:
            print(' ' * (spaces + 1), '*')
            print(' ' * spaces, '*' * (stars * 2 + 1))
        else:
            print(' ' * spaces, '*' * (stars * 2 + 1))

        spaces -= 1
        stars += 1


create_pyramid(
    random.randint(2, 10)
)
