import os
import geopandas as gpd


input_dir = 'data'
input_filename ='karnataka.gpkg'
file_path = os.path.join(input_dir, input_filename)

output_dir = 'data'
output_filename = 'national_highway_by_length.csv'
output_path = os.path.join(output_dir, output_filename)


read_gdf = gpd.read_file(file_path, layer='karnataka_major_roads')

district_gdf = gpd.read_file(file_path, layer='karnataka_districts')


## Filter the National highway roads from the major Roads
## Add a column called length and calculate the lenght of each geometry

def national_highway():

    filtered_national_highway = read_gdf[read_gdf['ref'].str.startswith('NH') == True]

    national_highway_reprojected = filtered_national_highway.to_crs('EPSG:32643') # Projected Coordinate

    national_highway_reprojected['length'] = national_highway_reprojected['geometry'].length # Length column in meter

    national_highway_with_length = national_highway_reprojected

    total_length = national_highway_reprojected['length'].sum() # suming all the length columns

    print('This is total length',total_length)

    return national_highway_with_length



## Use spatial_Join to join National Highway and District Dataframe
def national_highway_within_each_district(national_highway):

    district_reprojected = district_gdf.to_crs('EPSG:32643')

    spatial_join = gpd.sjoin(national_highway, district_reprojected, how='left', predicate='intersects')


    return spatial_join


## Sum up all the National Highway within each district

def total_highway_length_within_each_district():

    n_highway = national_highway()
    spatial_join = national_highway_within_each_district(n_highway);

    results = (spatial_join.groupby('DISTRICT')['length'].sum()/1000).round(2)
    
    ## Group each district together and sum up their length in km

    results = results.reset_index(name='total_highway_length')

    results.to_csv(output_path, index=False)

    print(results)



total_highway_length_within_each_district()

## NOTE

# Spatial Join (Left Join)
# Keep all roads from the LEFT GeoDataFrame.
# Find districts from the RIGHT GeoDataFrame that intersect each road.
# Add matching district information to the road records.
# Roads without a matching district are kept with NaN district values.
# A road intersecting multiple districts can appear multiple times.