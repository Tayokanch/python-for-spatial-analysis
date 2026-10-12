## Loops and Conditionals

### For Loops : This loops is used for iterating over a sequence. The sequence can be a List, a Tuple, a Dictionary, a Set, or a String

#### For Loops for List
cities = ['San francisco', 'Los Angeles', 'New york', 'Atlanta']

for city in cities:
    print(city);
print('_________________________________')
#### For Loops for Dictionaries

data = {'city': 'San Francisco', 'population': 881549, 'coordinate': (-122.4194, 37.7749)}

for info in data.items():
    print(info)
print('_________________________________') 

for key, value , in data.items():
    print(f'The key {key.upper()} and the value is {value}')

print('_________________________________') 
## How to iterate for a given time

for x in range(5):
    print(x);

print('_________________________________') 
for x in range(1, 10): ## start from 1 and stop at 10
    print(x);

print('_________________________________') 

for x in range(0, 10, 2): ## start from 1 and stop at 10 but skip every second number
    print(x);

print('_________________________________') 


## Conditions

for city in cities:
    if city == 'Atlanta':
        print(city)
    else:
        print('Atlanta isn\'t part of the list', )

print('_________________________________') 

for num in range(20):
    if num % 2 == 0:
        print(f'{num} is an even number');
    else:
        print(f'{num} is an odd number');

print('_________________________________') 


cities_population = {
    'San Francisco' : 881549,
    'Los Angeles' : 3792621,
    'New York': 8175133,
    'Atlanta': 498044
};


for city, population, in cities_population.items():
    if population < 1000000:
        print(f'{city.upper()} is a small city')
    elif population > 1000000 and population < 5000000:
        print(f'{city.upper()} is a big city')
    else:
        print(f'{city.upper()} is a mega city')


## Controlled Statement
### This is used for stopping a loop was once the condition has been met in other to save our compute resources

### BREAK
### A break statement will stop the loop and exit out of it. This is the most commonly used one

for city in cities:
    if city == 'Los Angeles':
        print('I found Los Angeles')
        break


### CONTINUE
### continue skips the remaining code in the current iteration when a condition is met and moves to the next iteration.

for city in cities:
    if city == 'New york':
        continue
    print(f'condition met, I am now moving to the next iteration where i found {city}')

## PASS

## Pass means do nothing

for x in range(10):
    pass;

for city in cities:
    if city == 'Los Angeles':
        pass
    else :
        print(city)