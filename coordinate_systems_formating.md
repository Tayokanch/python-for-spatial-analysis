# Coordinate Formats and Precision

* `X and Y `oordinates helps you to uniquely locate a place on the Earth
  
* There are 2 primary types of  Coordinate Reference Systems
  * Geographic CRS: This uses `Latitude` and `Longitude` as coordinate on a sphrerical/ellipsiodal model of the earth
  * Projected CRS: This uses X and Y coordinate on a planar (flat) projected surface
  
* In a Geographic CRS ( such as WGS84),**`X Coordinate is the Longitude`** and **`Y coordinate is the Latitude`**
  * Coordinate values are commonly stored in the following formats
    * **Degrees, Minutes, Seconds**
        - This allows concise way to capture high-degree of precision
        - Coordinate has 3 parts:
          - Degress
          - Minutes(1 degree = 60 minutes)
          - Seconds 1 minute = 60 seconds
        - Latitude values range from `0 to 90 degrees at North Pole` and` -90 degrees at South Pole`, `0 to plus 180 degrees towards the East` and `-180 towards the West
        - This Coordinate is used for physical maps and displays
        - So Latitude values ranges from 0 to 90 degrees
        - Longitude  values ranges from 0 to 180 degrees
  

    * **Decimal Degrees**
      * Allows ease of calculations and storage
      * Coordinate are stored as decimal numbers
      * latitude values ranges from -90 degress to 90 degress
        * North is positive(+) and South is negative(-)
        * East is positive(+) and West is negative(-)
      * Used for data storage and analysis

# CONVERSION of COORDINATE

## How to convert **Degrees, Minutes, Seconds** to **Decimal Degrees**

*Latitude* = **12 58' 20'' N**

*Longitude* = **77 34' 50'' E**

*Latitude Conversion* = 12 + 58/60 + 20/3600
*Latitude in Decimal Degress* = 12.97222222

*Longitude Conversion* = 77 + 34/60 + 50/3600
*Longitute in Decimal Degress* = 77.58055556



## Note : if the DMS coordinates degrees are >0 we will use minus(-) for the arithmetic/ conversion

