import os
from filtering_data import my_city_coordinate
from filtering_data import cities_within_my_countries
from geopy import distance

output_filename = 'cities_distances.csv'
output_dir = 'data'
output_path = os.path.join(output_dir, output_filename)


def calculate_distance(row):
    other_city_coordinate = (row['lat'], row['lng']) ## Takes The lat and lng on each row
    my_coordinate= my_city_coordinate('United Kingdom', 'Manchester')
    return distance.geodesic(my_coordinate, other_city_coordinate).km

my_country_df = cities_within_my_countries('United Kingdom', 'Manchester');

my_country_df['distance'] = my_country_df.apply(calculate_distance, axis=1); ## It will create a column called distance in the my_country_df
filtered = my_country_df.loc[:, ['city', 'distance']] # Output the dataframe with all the rows and just city and distance columns
renamed_column = filtered.rename(columns= { 'distance': 'distance_km2'})

renamed_column.to_csv(output_path, index=False) ## Saved to output_path

print(renamed_column)