from pathlib import Path

import pandas as pd

# step 1: load student rows from CSV
data_dir = Path(__file__).resolve().parent.parent / "data"
df = pd.read_csv(data_dir / "students.csv")
df.columns = df.columns.str.lower()

# step 2: print the original data set (column -> list, like a dict of columns)
data = df.to_dict("list")
print("\nOriginal data set:")
print(data)

# step 3–4: DataFrame is already built from the file
print("\nDataFrame:")
print(df)

# step 5: Question 1: names with age > 20 (without pandas-style indexing on lists)
print("\nWithout pandas:")
for i in range(len(data["age"])):
    if data["age"][i] > 20:
        print(data["name"][i])

# step 6: Question 2: Who is the oldest student?
print("\nWith pandas:")
oldest_student = df[df["age"] == df["age"].max()]
print(oldest_student)

# step 7: Question 3: Add a new column
df["grade"] = df["gpa"] * 10
print("\nDataFrame with new column:")
print(df)

# step 8: add new column (senior) df['senior'] = df['age'] > 20
df["senior"] = df["age"] > 20
print("\nDataFrame with new column (senior):")
print(df)

# step 9: Quick Analysis: Count by major
print("\nQuick Analysis: Count by major?")
print(df["major"].value_counts())

# step 10: Quick Analysis: Mean GPA by major
print("\nQuick Analysis: Mean GPA by major?")
print(df.groupby("major")["gpa"].mean())
