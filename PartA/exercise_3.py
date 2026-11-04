a = float(input("Enter side a's length: "))
b = float(input("Enter side b's length: "))
c = float(input("Enter side c's length: "))

def caclulate_area(a, b, c):
    # using herons formula
    semiperimeter = (a + b + c) / 2
    area = (semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)) ** 0.5

    return round(area, 2)

print(f"The area of your triangle is {caclulate_area(a, b, c)}")