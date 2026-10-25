import time
from geopy.geocoders import Nominatim


address = [('Rusland Court, M9 7HG'), ('10 Overlinks Road, M11 3DD'), ('Wester Hill Road, OL8 2QH')]

def geocode_address():
    geolocator = Nominatim(user_agent="manchester_geocoding_exercise")
    locations = []

    for add in address :
        result = geolocator.geocode(add)
        if result is not None:
            locations.append({"address": add, "coordinate":(result.latitude, result.longitude)})
        else:
            print(f'Address not found: {add}')
        time.sleep(1)
    return locations

print(geocode_address())