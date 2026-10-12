# Functions

def greet(name):
    return f'Hello, {name}'

result = greet('tayo');
print(result);

print("________________________________")

def calculate_density(population, area_sqmi):
    return f'{round(population / area_sqmi, 2)} sqmiles'

density = calculate_density(881549, 46.89)
print(density)

def dms_to_decimal(degrees, minutes, seconds):
    if degrees > 0:
        result = degrees - minutes/60 - seconds/3600
    else:
        result = degrees + minutes/60 + seconds/3600
    return result;


output = dms_to_decimal(10, 10, 10)

print(f'Coordinate in decimal degree {output}')

