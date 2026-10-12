# Data Structures

## Tuples
### Tuples : A tuple is a sequence of objects. It can have any number of objects inside. In python tuples are written in round brackets ().
### Tuples: can be simple be used for used for storing multiple values in a single variable

latitude = 37.7739
longitude = -121.5687
cordinate = (latitude, longitude); "This is a Tuple"

print("The cordinate of this area is", cordinate);


### A Tuple can also contain different data types:

location = ("Lagos", 6.5244, 3.3792, True)

### Tubles also have an list behavior where we can extract values based on their index

state = location[0]
the_latitude = location[1]
the_longitude = location[2]
status = location[3]
      
"____________________________________________________________"

## List

### A List is similar to a tuple but with a a key difference. With Tuples, once created, they can't be changed i.e they are immutable. 
### But Lists are mutable i.e, you can add, delete or change the elements within a List. In python, list are written with square brackets []

cities = ['San Francisco', 'Los Angeles', 'New York', 'Atlanta']

print(cities)
print(cities[0]) 
print(len(cities)) ## len(), this is use to determine the length of a list

print("--------------")

cities.append('Boston') ## append(), This is used to add an element to a list, and it becomes the last new element in the list
print(cities);

print("--------------")

cities.sort(); ## sort(), this is use for sorting elements in an Ascending order
print("Sorting Cities in an Ascending order",cities);

print("--------------")

cities.sort(reverse=True); ## (reverse=True), this is use for sorting elements in a Descending order
print("Sorting Cities in an Descending order",cities);

print("--------------")

"____________________________________________________________"

## Sets
### Sets are like lists, but with some intersecting properties. Mainly that they contain only unique values.
### It also allow for set operations such as (intersection, union, and difference)
### It is also used for creating distinct values in a List

## Example here: we want to determine which city is also a capital using the both cities and capital Lists
capitals = ['Sacremento', 'Boston', 'Austin', 'Atlanta']

capitals_set = set(capitals); ## turns capital into a object in an order
cities_set = set(cities); ## turns cities into a object in an order

print(capitals_set, ",", cities_set); 
#### {'Boston', 'Austin', 'Atlanta', 'Sacremento'} , {'Boston', 'New York', 'Atlanta', 'San Francisco', 'Los Angeles'}
capital_cities = capitals_set.intersection(cities_set) ## intersect both object and return elements of the same values

print("Capital City:", capital_cities);

#### Capital City: {'Boston', 'Atlanta'}

### Note: we can also do this for difference and union

"____________________________________________________________"

## Extend

### This is a built in method to join two a list to another list

print(cities.extend(capitals));

print("extend cities:", cities)

print("These are distinct cities after joining", set(cities));

"____________________________________________________________"
print("____________________________________________________________")
## Dictionaries

### In python dictionaries are written with curly brackets {}. Dictionaries have keys and values. 
### With lists, we can access each element by its index. But a dictionaries makeit easy to access by name, Keys and values

data = {'City': 'San Francisco', 'Population': 881549, 'Coordinate': (-122.4194, 37.7749)}
data['City']
data['Population']
print('The coordinate is', data['Coordinate'])


