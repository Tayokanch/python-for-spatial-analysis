import os
import pandas as pd
from working_with_pandas import df


def filter_country(country):
    global df;
    country = df[df['country'] == country]
    print(country)
    return country

def cities_within_my_countries(my_country, my_city):

    global df;
    cities = df[(df['country'] == my_country) & (df['city'] != my_city)].copy()
    print("This is the DF of the cities within my Country", cities)
    return cities;


def filter_country_per_population(country, population_size):
    global df;

    filter_cities_with_population_size = df[(df['country'] == country) & (df['population'] > population_size)]

    print(f'Cities with population of 500,000 and above in the UK are: {filter_cities_with_population_size}')

    return filter_cities_with_population_size;

filter_country_per_population('Nigeria', 800000)
filter_country_per_population('United Kingdom', 500000)


def northern_hemispere_cities():
    global df;
    cities = df[df['lat'] > 0]

    print(cities.head())
    return cities

def southern_hemispere_cities():
    global df;
    cities = df[df['lat'] < 0]

    print(cities.head())
    return cities

def my_city_coordinate(country,city):
    global df;
    filtered_city = df[(df['country'] == country) & (df['city'] == city)].iloc[0]## The Copy() method is used for saving the filtered view to a new Dataframe
    coordinate = (filtered_city['lat'], filtered_city['lng'])
    print((f'The Coordinate of {city} is: {coordinate}'))
    return coordinate;

northern_hemispere_cities();
southern_hemispere_cities();
my_city_coordinate('United Kingdom', 'Manchester')


## NOTE

"""In pandas, the .copy() method creates an independent copy of a DataFrame or a selected portion of it, 
allowing you to modify the copied data without changing the original DataFrame."""