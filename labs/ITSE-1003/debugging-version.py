import pandas as pd
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent / "data"

# WEEK 3 MINI LAB - DEBUGGING VERSION
# This program has 5 errors. Find and fix them.

 
#df = pd.read_csv("student.csv") # error: file not found
df = pd.read_csv(_DATA_DIR / "students.csv")

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET INFO ---")
print(df.info())

print("\n--- STUDENTS OLDER THAN 21 ---")
#filtered = df[df["age"] > 21] # error: age is not a valid column name
filtered = df[df["Age"] > 21]
print(filtered)

# create a new column Status based on the Grade
status_list = []

# loop through the Grade column and add the status to the status_list
for grade in df['Grade']: # error: Grade is not a valid column name
    if grade > 70:
        status_list.append('Pass')
    else:
        status_list.append('Fail')

# add the new column to the dataframe
# df["Status"] == status_list  # error: == compares; use = to assign the column
df["Status"] = status_list
#print("\nStatus:")
#print(df["Status"])

print("\n--- DATA WITH STATUS COLUMN ---")
print(df)

print("\n--- STUDENTS PER MAJOR ---")
major_counts = df.groupby("Major").count()
print(major_counts)

print("\n--- SORTED BY AGE ---")
#sorted_df = df.sort_value("Age") # error: sort_value is not a valid method
sorted_df = df.sort_values("Age")
print(sorted_df)

print("\n--- AVERAGE GRADE PER MAJOR ---")
avg_grade = df.groupby("Major")["Grade"].mean()
print(avg_grade)

print("\n--- HIGHEST GRADE ---")
highest_grade = df["Grade"].max()
print(highest_grade)

print("\n--- STUDENT(S) WITH HIGHEST GRADE ---")
top_students = df[df["Grade"] == highest_grade]
print(top_students)

#df.to_csv("students_output.csv", index=false) # error: false is not a valid value for index
df.to_csv("students_output.csv", index=False)

print("\nFile exported as students_output.csv")
print("\n--- END OF PROGRAM ---")
