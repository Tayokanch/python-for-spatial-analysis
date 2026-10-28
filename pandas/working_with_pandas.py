import os;
import pandas as pd;

dir = 'data'
filename = 'worldcities.csv'
filepath = os.path.join(dir, filename)

## pd.read_csv() To read a CSV file
## pd.read_excel() To read an EXCEL file
## pd.read_hdf() To read an HDF file

df = pd.read_csv(filepath)
print(df) ## This prints the first 5 rows and the last 5 rows

print('______________________')

## To get the first 5 rows 
df.head() 

## To get the last 5 rows
df.tail() 

print('______________________')

## To get information of the dataframe

## print(dataframe.info()) 


## Selecting by Index

## Select first 5 rows and first 5 columns
## dataframe.iloc[0:5,0:5 ]

## Select every alternate row in reverse order

df.iloc[::, -2 ]

## Selecting by label

'''df.loc['column_label', 'column_label']'''

'''df.loc['city', 'country']'''

## Shortcut

'''df['column_label', 'column_label']'''