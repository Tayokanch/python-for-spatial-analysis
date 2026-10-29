## Geopandas

- **Geopandas** extends the pandas library to enable spatial operations
  
- **Geopandas** is built on top of the following libraries that allows it to be spatially aware.
  - `Shapely` for geometric operation (i.e, buffer, intersection etc)
  - `PyProj` for working with projections
  - `Fiona` for file input and output, which itself is based on the widely used GDAL/OGR library
  
- **Geopandas** provides built-in functions for
  - Geoprocessing (`buffer`, `intersection`, `dissolve` etc)
  - Joins (table join, spatial join etc)
  - Transformation (reproject, filter etc)
  - Format Conversion

### Basic Terminology

- **GeoDataframe**: A tabular structure with a geometry (point, line, and polygon)
- **Geoseries**: A structure that holds geometry
  