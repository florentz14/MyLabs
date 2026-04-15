# ------------------------------------------------------------ #
# File: lab2_preview.py
# Date: 2026-04-15
# Author: Florentino
# Description: Load lab2_students.csv and preview data and columns.
# Explanation: It explains load lab2_students.csv and preview data and columns and why it is useful in basic data analysis.
# ------------------------------------------------------------ #


import pandas as pd

from config import data_file

file_path = data_file("lab2_students.csv")

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Print the DataFrame
print(df)

# Print the column names
print(df.columns)
