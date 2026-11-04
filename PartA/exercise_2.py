distance = float(input("Enter the distance in miles: "))
fuel_efficency = float(input("Enter the fuel effeciency in MPG: "))
petrol_price = float(input("Enter the petrol price per litre: "))

def calculate_fuel_cost(distance, mpg, price_per_litre):
    gallons_conversion = 4.546
    price_per_litre *= gallons_conversion
    price_per_litre /= mpg

    return round(distance * price_per_litre, 2)


print(f"Your estimated fuel cost is: £{calculate_fuel_cost(distance, fuel_efficency, petrol_price)}")