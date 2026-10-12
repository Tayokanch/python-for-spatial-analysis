## Exercise 1

##Given a coordinate string with value in degree, minutes and seconds, convert it to decimal degrees by calling the `dms_to_decimal` function.
# Add the code below to extract the parts from the coordinate string,
# call the function to convert to decimal degrees and print the result
# The expected answer is 37.773972


def dms_to_decimal(coordinate):
    degree = int(coordinate.split()[0][0:2])
    minutes = int(coordinate.split()[1][0:2]) / 60
    seconds = float(coordinate.split()[2][0:7]) / 3600
    if degree < 0:
       return degree - minutes - seconds
    else: 
        return degree + minutes + seconds


coordinate = '''37° 46' 26.2992"'''
print(dms_to_decimal(coordinate))

"____________________________________________"

# Exercise 2
# Once you are done with the exercise, you can attempt this challenge. Can you implement a function decimal_to_dms() which does the reverse operation? i.e. convert decimal degrees to degrees,minutes and seconds?

def decimal_to_dms(coordinate):
    degree = int(coordinate)
    decimal_minutes = (coordinate - degree) * 60
    decimal_seconds = (decimal_minutes - int(decimal_minutes)) * 60
    result = f'{degree}° {round(decimal_minutes)}\' {round(decimal_seconds, 4)}"'
    return result;


print(decimal_to_dms(37.773972))