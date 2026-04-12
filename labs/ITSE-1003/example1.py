# File: example1.py
# Date: 2026-04-11
# Author: Florentino
# Description: Example 1 of the ITSE 1003 course.
#-------------------------------------------------


import pandas as pd

from config import data_file

file_path = data_file("lab2_students.csv")

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Print the DataFrame
print(df)

# Print the column names
print(df.columns)