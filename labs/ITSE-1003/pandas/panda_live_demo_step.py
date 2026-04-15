from pathlib import Path

import pandas as pd

# step 1: load student rows from CSV
data_dir = Path(__file__).resolve().parent.parent / "data"
df = pd.read_csv(data_dir / "students.csv")
df.columns = df.columns.str.strip()

# step 2: print the full DataFrame
print("\nDataFrame:")
print(df)

# step 3: show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# step 4: show last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# step 5: show DataFrame info (columns, dtypes, non-null counts, memory)
print("\nInfo:")
print(df.info())

# step 6: show numeric summary statistics (mean, std, min, max, count)
print("\nDescribe:")
print(df.describe())

# step 7: show column names
print("\nColumns:")
print(df.columns)

# step 8: select one column
print("\nSelect one column:")
print(df["Name"])

# step 9: select multiple columns
print("\nSelect multiple columns:")
print(df[["Name", "Age", "Major"]])

# step 10: select rows using loc with a boolean condition
print("\nSelect rows using the loc method:")
print(df.loc[df["Age"] > 30])

# step 11: select rows using slice notation (row positions)
print("\nSelect rows using the slice operator:")
print(df[0:3])

# step 12: select a single row by integer position with iloc
print("\nSelect rows using the iloc method:")
print(df.iloc[0])

# step 13: filter rows with a boolean mask (Age > 30)
print("\nSelect rows where Age is greater than 30:")
print(df[df["Age"] > 30])

# step 14: filter students older than 20 using loc
print("\nFilter students older than 20 using the loc method:")
print(df.loc[df["Age"] > 20])

# step 15: same filter via iloc (integer row positions from the boolean mask)
print("\nFilter students older than 20 using the iloc method:")
print(df.iloc[(df["Age"] > 20).to_numpy().nonzero()[0]])

# step 16: select first three rows using slice notation
print("\nFilter students older than 20 using the slice operator:")
print(df[0:3])

# step 17: filter students with grade letter A using loc
print("\nFilter students with grade letter A using the loc method:")
print(df.loc[df["grade_letter"].str.strip() == "A"])

# step 18: filter students with grade greater than 70 using loc
print("\nFilter students with grade greater than 70 using the loc method:")
print(df.loc[df["grade"] > 70])

# step 19: add a new column Passed (grade >= 70)
df["Passed"] = df["grade"] >= 70
print("\nDataFrame with new column (Passed):")
print(df)

# step 20: add column Status (Passed/Failed) with apply and a lambda
df["Status"] = df["grade"].apply(lambda x: "Passed" if x >= 70 else "Failed")
print("\nDataFrame with new column (Status):")
print(df)

# step 21: sort students by age descending
print("\nSort students by age in descending order:")
print(df.sort_values(by="Age", ascending=False))

# step 22: sort students by age ascending
print("\nSort students by age in ascending order:")
print(df.sort_values(by="Age", ascending=True))

# step 23: group by major and count rows
print("\nGroup students by major and count the number of students:")
print(df.groupby("Major").size())

# step 24: average grade per major
print("\nAverage grade per major:")
print(df.groupby("Major")["grade"].mean())

# step 25: student(s) with the highest grade
print("\nStudent with the highest grade:")
print(df[df["grade"] == df["grade"].max()])

# step 26: student(s) with the lowest grade
print("\nStudent with the lowest grade:")
print(df[df["grade"] == df["grade"].min()])

# step 27: student(s) with the highest GPA
print("\nStudent with the highest GPA:")
print(df[df["GPA"] == df["GPA"].max()])

# step 28: combine conditions with & (use parentheses; & binds tighter than >)
print("\nSelect rows where Age is greater than 30 and Major is Computer Science:")
print(df[(df["Age"] > 30) & (df["Major"] == "Computer Science")])

# step 29: save the updated DataFrame to a new CSV file
print("\nSave the updated DataFrame to a new CSV file:")
df.to_csv(data_dir / "students_updated.csv", index=False)
