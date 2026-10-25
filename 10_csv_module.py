import os
import csv
from geopy import distance

dir = 'data'
filename = 'worldcities.csv'
file_path = os.path.join(dir, filename)

with open(file_path, 'r', encoding='utf-8-sig') as file :
    
    csv_reader = csv.DictReader(file)

    for index, city in enumerate(csv_reader):
        print({'name': city['city'], 'coordinate': (city['lat'], city['lng'])})        
        if index == 5 :
            break;

resident_country = 'United Kingdom'
resident_city = 'Manchester'
resident_city_coordinate = ()
cities_within_resident_country = []
cities_number = 0  


def number_of_cities_in_country():
    global cities_number
    with open(file_path, encoding='utf-8-sig') as file :
        csv_reader = csv.DictReader(file)
        for  row in csv_reader:
            if resident_country.upper() == row['country'].upper():
                cities_number += 1
        print(cities_number)


def my_city_coordinate():

    with open(file_path, encoding='utf-8-sig') as file :
        global resident_city_coordinate
        csv_reader = csv.DictReader(file)
        for row in  csv_reader:
            if resident_city.upper() == row['city'].upper():
                lat = row['lat']
                log = row['lng']
                resident_city_coordinate = (lat, log)
        print(resident_city_coordinate)

## write the cities distance to a CSV file
def write_distance_to_home_city():
    output_filename = 'cities_distance.csv'
    output_path = os.path.join(dir, output_filename)
    fieldnames = ['city', 'distance_from_home']

    with open(output_path, 'w', newline='', encoding='utf-8-sig') as out_file :
        csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        csv_writer.writeheader();

        with open(file_path, encoding='utf-8-sig') as file :
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if(resident_country.upper() == row['country'].upper() and
                    resident_city.upper() != row['city'].upper()):
                    city_coordinate = (row['lat'], row['lng'])
                    city_distance = distance.geodesic(city_coordinate,resident_city_coordinate).km
                    csv_writer.writerow(
                        {'city': row['city_ascii'],
                        'distance_from_home': city_distance
                        }
                
        )



number_of_cities_in_country()
my_city_coordinate()
write_distance_to_home_city()