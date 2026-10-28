# Pandas

## What is Pandas

- Pandas is powerful library for working with tabular data e.g cvs, shapefile, etc
- Provides fast and easy functions for reading data from files, analyzing it
- Can read data from `Csv`, `Excel`, `HDF` and many other formats
- It gives Built-in functions for:
  - Data cleaning(remove duplicate, remove null values)
  - Data transformation (pivot, unpivot, merge, remove)
  - Group Statistics
  - Time-series processing (interpolation, gap-filling)
- Pandas implementation is very fast and efficient

## Basic Termimology in Pandas

- **Dataframe**: Two-dimensional data strucsture with rows and columns. Think of **Dataframe** as an **Excel Spreesheet** or an **Attribute Table** of a GIS layer that has `rows` and `columns`

- **Series**: one-dimensional data structure with labeled data. Think of a **Series** as a `single row` or a `single column`


## Pandas Selection

- All rows in a dataframe has an implicit index

- All columns in a dataframe has a implicit index and labe
  
- Each row or column in a Dataframe is assigned an Index or Label
  
- To select a row/column by index - use `.iloc[row_index, column_index]`
  
- To select a row/column by label - use `.loc[row_label, column_label]`
  

## Filtering Dataframes

- We can filter records using the syntax: `df[condition]`

- **Logical Operators**
  
  - filter rows matching a condition using `df[df['col_label'] > 10]` : returns rows where column 'col_label' is `greater than` 10
  
  - df[df['col_label'] != 'x'] : returns rows where column 'col_label' is `not equal to` x
  
  - df(df['col_label1'] == 'x') & (df['col_label2'] == 'y'): returns rows that meet both condation with column 'col_label1' and 'col_label2'

- **str accessor**: str allows us to work with columns or rows value
  
    - df[df['col_label'].str.startswith('A')] : returns all the columns whose values start with A
    - df[df['col_label'].str.match('A*')]

- **isin operator**
  - df[df['col_label'].isin(['A', 'B'])]: 
    Checks every row in the col_label column. It returns a Series of True/False values (True if the row contains 'A' or 'B', False otherwise).

- Many other functions for filtering null values, duplicates etc (Search Google)



## Performing Calculations
- **Simple Computations**
  - df['col_label']* 10 (vectorised operation)

- **Simple Statistics**
  - df['col_label'].sum()
  - df['col_label'].round()

- **Complex Calculations**
  - df.apply(function, axis)


## Note:
 
- axis 0 : row
- axis 1 : column