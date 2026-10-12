## The Python Standard Library

### Python comes with built-ib modules that offrs ready-to-use solution to common programming problems
### To use this modules, you have to import them using the keyword `import` Examples.

### Visist: https://docs.python.org/3/library/index.html To see all the built in python function

import math
from math import pi

print(math.sqrt(4))

## Calculating Distance btw 2 cities using Spere Earth Surface

"""""
Given 2 points with their Latitude and Longitude Coordinate, the Haversine Formula,
Calculate the straight-line distance in meters, assuming the Earth is a Spere
"""""

manchester_picadilly_station = (53.4767, -2.2290)
london_euston_station = (51.528664, -0.133296)

def haversine_formula(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371000
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)* math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c
    return distance

distance = haversine_formula(manchester_picadilly_station, london_euston_station)

print(distance/1000, 'km')