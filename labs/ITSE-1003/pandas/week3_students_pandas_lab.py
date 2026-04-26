from pathlib import Path

import pandas as pd

# week 3 mini lab: read data.json and print the data

_DATA_DIR = Path(__file__).resolve().parent / "data"

# load the data set from students.csv (path works no matter the cwd)
df = pd.read_csv(_DATA_DIR / "students.csv")

#print the data
print("Original Data:")
#print(df)

#print the column names
print("Column Names:")
#print(df.columns)

#print the number of rows and columns
print("Number of Rows and Columns:")
#print(df.shape)

#print the first 5 rows
print("First 5 Rows:")
#print(df.head())

#print the last 5 rows
print("Last 5 Rows:")
#print(df.tail())

# display general information about the data
print("General Information:")
print(df.info())

# display the summary statistics of the data
print("Summary Statistics:")
#print(df.describe())

# display the column names and their data types
print("Column Names and Data Types:")
#print(df.dtypes)

# operation filters students older than 20
print("Students Older than 20:")
#print(df[df['Age'] > 20])

#create a new column Status based on the Grade
status_list = []
for grade in df['Grade']:
    if grade > 70:
        status_list.append('Pass')
    else:
        status_list.append('Fail')

# add the new column to the dataframe
df['Status'] = status_list
print("\nStatus:")
print(df['Status'])

# calculate the average grade of the students per major
print("\nAverage Grade per Major:")
average_grade = df.groupby('Major')['Grade'].mean()
print(average_grade)

# Find de highest grade
print("\nHighest Grade:")
max_grade = df['Grade'].max()
print(max_grade)

# output export the dataframe to a csv file
df.to_csv(_DATA_DIR / "students_status.csv", index=False)
print("\nExported to students_status.csv")
print(df)
