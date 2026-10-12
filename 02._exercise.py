##Exercise

### From the dictionary below, how do you access the latitude and longitude values? print the latitude and longitude of new york city by extracting it from the dictionary below.

nyc_data = {'city': 'New York', 'population': 8175133, 'coordinates': (40.661, -73.944) }
latitude = nyc_data['coordinates'][0]
longitude = nyc_data['coordinates'][1]

print("latitude:", latitude , "and", "longitude:", longitude)