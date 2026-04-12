# -------------------------------------------------
# File Name: ITSE-1003/Lab2CSV/lab2_csv_manipulation_pandas.py
# Author: Florentino Baez
# Course: ITSE-1003 (Python for Data Science)
# Professor: Mauricio Quiroga
# Date: 3/27/2026
# Description: Lab 2 - Same tasks as lab2_csv_manipulation.py using pandas (read_csv, filters, groupby).
# Requires: pip install pandas
# -------------------------------------------------

from pathlib import Path
from typing import cast

import pandas as pd

# Paths next to this script (works regardless of current working directory)
_LAB_DIR = Path(__file__).resolve().parent
_DATA_DIR = _LAB_DIR / "data"
_GENERATED_DIR = _LAB_DIR / "generated"
CSV_PATH = _DATA_DIR / "lab2_students.csv"
SUMMARY_PATH = _GENERATED_DIR / "lab2_summary_pandas.txt"


# -------------------------------------------------
# Task 1 - Import and open the file (pandas read_csv)
# -------------------------------------------------
_GENERATED_DIR.mkdir(parents=True, exist_ok=True)

# dtype ensures Age/GPA are numeric for analysis; column names match the CSV header.
students = pd.read_csv(
    CSV_PATH,
    encoding="utf-8",
    dtype={"Name": str, "Last_Name": str, "Email": str, "Major": str},
)
# Convert Age and GPA to integers and floats respectively.
students["Age"] = students["Age"].astype(int)
students["GPA"] = students["GPA"].astype(float)


# -------------------------------------------------
# Task 2 - Print all students in a clean format
# -------------------------------------------------
print("\n--- Task 2: All Students ---")
for _, row in students.iterrows():
    print(
        f"Name: {row['Name']} | "
        f"Age: {row['Age']} | "
        f"Major: {row['Major']} | "
        f"GPA: {row['GPA']}"
    )


# -------------------------------------------------
# Task 3 - Calculate the average age
# -------------------------------------------------
average_age = cast(float, students["Age"].mean())
print(f"\nAverage age: {average_age:.1f}")


# -------------------------------------------------
# Task 4 - Find the oldest student
# -------------------------------------------------
_i_oldest = int(students["Age"].to_numpy().argmax())
print(
    f"\nOldest student: {students['Name'].iloc[_i_oldest]} "
    f"({int(students['Age'].iloc[_i_oldest])} years old)"
)


# -------------------------------------------------
# Task 5 - Print only Computer Sci students
# -------------------------------------------------
print("\n--- Computer Sci Students ---")
cs_only = students[students["Major"] == "Computer Sci"]
for name in cs_only["Name"]:
    print(name)


# -------------------------------------------------
# Task 6 - Count how many students are in each major
# -------------------------------------------------
# sort=False keeps majors in order of first appearance (same idea as the dict-based lab)
major_count = students.groupby("Major", sort=False).size()
print("\n--- Students per Major ---")
for major, count in major_count.items():
    print(f"{major}: {cast(int, count)}")


# -------------------------------------------------
# Task 7 - Print students with GPA 3.5 or higher
# -------------------------------------------------
print("\n--- Students with GPA >= 3.5 ---")
high_gpa = students[students["GPA"] >= 3.5]
for name in high_gpa["Name"]:
    print(name)


# -------------------------------------------------
# Stretch challenge
# -------------------------------------------------
average_gpa = cast(float, students["GPA"].mean())
print(f"\nAverage GPA: {average_gpa:.2f}")

print("\n--- Students older than 21 ---")
over_21 = students[students["Age"] > 21]
for name in over_21["Name"]:
    print(name)

with SUMMARY_PATH.open(mode="w", encoding="utf-8") as summary_file:
    summary_file.write("Lab 2 Summary (pandas)\n")
    summary_file.write("-----------------\n")
    summary_file.write(f"Average Age: {average_age:.1f}\n")
    summary_file.write(f"Average GPA: {average_gpa:.2f}\n")
    summary_file.write("Students older than 21:\n")
    for name in over_21["Name"]:
        summary_file.write(f"- {name}\n")

print(f"\nSummary written to {SUMMARY_PATH.name}")
