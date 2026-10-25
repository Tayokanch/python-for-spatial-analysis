import os 
import csv
dir = 'data'
filename = 'worldcities.csv'
file_path = os.path.join(dir, filename)

##reading a file 
with open(file_path, 'r', encoding='utf-8-sig') as file :
    rows = csv.DictReader(file)

    for row in rows:
        print(row)


##creating and writting  a file 

output_file = 'test.txt'
output_path = os.path.join('data', output_file)
print(output_path)

with open(output_path, 'w', encoding='utf-8-sig') as file :
    file.write("Hello")


## reading first 5 lines

with open(file_path, 'r', encoding='utf-8-sig') as file :
    rows = csv.DictReader(file)
    count = 0
    for row in rows:
        print(row)
        count+= 1
        if count == 5:
            break;
