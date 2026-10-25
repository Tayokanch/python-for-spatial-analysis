import time
from geopy.geocoders import Nominatim


## This exercise is about Geocoding address using `GeoPy`
## What is Geocoding: This is a process of turning address to a Lat & and Log coordinate
# List of Hurricane Evacuation Centers in New York City with Addresses


locations = [
    ('Norman Thomas HS (ECF)', '111 E 33rd St, NYC, New York'),
    ('Midtown East Campus', '233 E 56th St, NYC, New York'),
    ('Louis D. Brandeis HS', '145 W 84th St, NYC, New York'),
    ('Martin Luther King, Jr. HS', '122 Amsterdam Avenue, NYC, New York'),
    ('P.S. 48', '4360 Broadway, NYC, New York')
]


def geocode_address():
    geolocator = Nominatim(user_agent="tayo_first_geocoding_practical")

    address = []

    for location in locations:
        result = geolocator.geocode(location[1])

        if result is not None:
            coordinate = (
                location[0],
                result.latitude,
                result.longitude
            )

            address.append(coordinate)

        else:
            print(f"Address not found: {location[1]}")

        time.sleep(1)

    return address


print(geocode_address())


