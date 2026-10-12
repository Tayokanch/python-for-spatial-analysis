## Third - Party Modules

### Python has a thriving ecosystem of third-party modules (i.e. Libraries or Packages)

### Python comes with a `package manager called pip`. 
### It can install all packages listed in at `PyPI(Python package Index)`
### To install a package using pip, you need to run command `pip install <package_name>


## However, I  will be using UV as my package manager

from geopy import distance
import xarray

manchester_picadilly_station = (53.4767, -2.2290)
london_euston_station = (51.528664, -0.133296)

## using a 3rd party library to calculate distance btw 2 locations on a spere surface
sphere_distance = distance.great_circle(manchester_picadilly_station, london_euston_station)
print(f'The distance btw Manchester Picadilly Station and London Euston Station is {sphere_distance} on an SPHERE surface')

"_______________________________________"

## using a 3rd party library to calculate distance btw 2 locations on a ellipsoid surface
### This is preferable and more accurate

ellipsoid_distance = distance.geodesic(manchester_picadilly_station, london_euston_station, ellipsoid='WGS-84')
print(f'The distance btw Manchester Picadilly Station and London Euston Station is {ellipsoid_distance.km} km on an ELLIPSOID surface')
print(f'The distance btw Manchester Picadilly Station and London Euston Station is {ellipsoid_distance.mi} miles on an ELLIPSOID surface')