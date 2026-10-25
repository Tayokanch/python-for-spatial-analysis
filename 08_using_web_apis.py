## Using Web APIs
import json;
import requests
import os
from dotenv import load_dotenv

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")


geojson_string = '''
{
"type": "FeatureCollection",
"features": [ 
    {
    "types": "feature",
    "properties": {"name": "San Francisco"},
    "geometry": {"type": "point", "coordinates":[-121.5687, 37.7739]}
    }
]
}
'''

data = (json.loads(geojson_string))
print(data['features'][0])

response = requests.get('https://diaryhubapi.tayolabs.dev/health')
print(response.status_code);


OSR_API_KEY = 'eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImRmMzJlMzFmMTA2ZDQzZWI4MDU4YjRhYjVkYzc2OWNkIiwiaCI6Im11cm11cjY0In0='


def check_distance(start_location, end_location, means_of_travelling):

    
    parameters = {
        'api_key' : OSR_API_KEY,
        'start_location' : '{},{}'.format(start_location[0],start_location[1]),
        'stop_location' : '{},{}'.format(end_location[0],end_location[1])
    }

    response = requests.get(f'https://api.openrouteservice.org/v2/directions/{means_of_travelling}', params=parameters)
    if response.status_code == 200:
        print('Request Successful.')
        data = response.json()
    else:
        print('Request Failed')

manchester_picadilly = (53.4774, -2.2309)
bolton_railway_station = (53.573, -2.425)

check_distance(manchester_picadilly, bolton_railway_station, 'driving-car')