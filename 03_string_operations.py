# String Operations

## Built in function and Method for String Operation 
city = 'San Francisco,California'

### len():  This is used to determine length of character of a string
### split() This is used for Breaking / splitng string into 2 part. It also accept an arguement of character to split string with character e.g(,) container in the string
### upper() ### To change string to UPPER CASE
### lower() ### To change string to LOWER CASE


print(city.split(',')) ## This split city with (,) and the output comes as a List ['San Francisco', 'California']
print(city.split(',')[0].upper()) 

"_____________________________________________________"

## String Index

city[0] ## first character of the string
city[-1] ## This use use to determine the last character of a string if we character are to long

##list[start:end:step]

city[0:4]  ## Extracts characters from index 0 up to, but not including, index 4.

city[4:] ## Extracts characters from index 4 up to the string


city[:]  ## Extracts characters from the begining of the index (0) to the last string

city[::2]  # Starts at index 0 and extracts every second character until the end of the string.


city[::-1]  # Extracts characters in reverse order, from the last character to the first.


"_____________________________________________________"

## Escaping characters in string 

### In python strings, the backlash (\) is a special character, also called the **escape character

my_string ='It\'s a beautiful day!' ## here we use backlash to escape the qoute in-btw the string

"""Problem 1: There could be situation there by our variable comes with a single quote and double quote E.g A Degree Mins Seconds Coordinate"""""
## coordinate = 40° 42′ 51″ N, 74° 0′ 21″ W , the solution would be to use a triple single quote to preserves both characters

correct_coordinate = '''40° 42′ 51″ N, 74° 0′ 21″ W''' ## This types of data are common when we use python to read degree mins seconds coordinate


"_____________________________________________________"

### Problem with backlash and it Solution

### when dealing with files path or Windows Path, it usually comes like:

### path = 'C:\Users\tayo\dev' ## The issue here is the backlash(\) is a spatial character, which would cause a 'unicode error'

"""Solution 1""" ### Its to use another backlash(\) to escape the first backlash(\) needed for the file path

correct_path = 'C:\\Users\\tayo\\dev'

print('path', correct_path);

"""Solution 2""" ### Declaring it as a (r string)
path = r'C:\Users\tayo\dev'


"_____________________________________________________"

## Printing Strings

### String format() Method

city = 'San Francisco'
poulation = 881549

output = 'Population of {} is {}'.format(city, poulation)

print(output)


### Latest Solution for String formating is using (f string)

new_output = f'Population of {city} is {poulation}';

latitude = 37.7749
longitude = -122.4194

coordinate = f'The coordinate are {latitude:.2f}, {longitude:.2f}' ## rounded them to a 2 decimal place

print(coordinate)
###:  Read more on f and r string  