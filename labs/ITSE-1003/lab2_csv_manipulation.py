# -------------------------------------------------
# File Name: ITSE-1003/Lab2CSV/lab2_csv_manipulation.py
# Author: Florentino Baez
# Course: ITSE-1003 (Python for Data Science)
# Professor: Mauricio Quiroga
# Date: 3/27/2026
# Description: Lab 2 - CSV manipulation with csv.DictReader, summaries, filters, stretch output.
# -------------------------------------------------

# import csv module to read the csv file
import csv

# import pathlib module to create file paths
from pathlib import Path

# Paths next to this script (works regardless of current working directory)
_LAB_DIR = Path(__file__).resolve().parent
# Course datasets and generated text output live under data/ (see labs/ITSE-1003/README.md)
_DATA_DIR = _LAB_DIR / "data"
_GENERATED_DIR = _LAB_DIR / "generated"

# create file path for the csv file
CSV_PATH = _DATA_DIR / "lab2_students.csv"

# create file path for the summary file (generated/ — not versioned; see .gitignore)
SUMMARY_PATH = _GENERATED_DIR / "lab2_summary.txt"


# -------------------------------------------------
# Task 1 - Import and open the file
# -------------------------------------------------
with CSV_PATH.open(mode="r", newline="", encoding="utf-8") as file:
    # read the csv file using csv.DictReader
    reader = csv.DictReader(file)

    # create a list to store the rows
    students = list(reader)

_GENERATED_DIR.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------
# Task 2 - Print all students in a clean format
# -------------------------------------------------
print("\n--- Task 2: All Students ---")

# print the students in a clean format
for student in students:
    print(
        f"Name: {student['Name']} | "
        f"Age: {student['Age']} | "
        f"Major: {student['Major']} | "
        f"GPA: {student['GPA']}"
    )


# -------------------------------------------------
# Task 3 - Calculate the average age
# -------------------------------------------------
# calculate the total age of the students
total_age = sum(int(s["Age"]) for s in students)

# calculate the number of students
num_students = len(students)

# calculate the average age of the students
average_age = total_age / num_students
print(f"\nAverage age: {average_age:.1f}")


# -------------------------------------------------
# Task 4 - Find the oldest student
# -------------------------------------------------

# find the oldest student using the max function and a lambda function
oldest_student = max(students, key=lambda s: int(s["Age"]))
print(
    f"\nOldest student: {oldest_student['Name']} "
    f"({oldest_student['Age']} years old)"
)


# -------------------------------------------------
# Task 5 - Print only Computer Sci students
# -------------------------------------------------
print("\n--- Computer Sci Students ---")
for student in students:
    # print the students with the major Computer Sci
    if student["Major"] == "Computer Sci":
        print(student["Name"])

# -------------------------------------------------
# Task 6 - Count how many students are in each major
# -------------------------------------------------
# create a dictionary to store the count of students in each major
major_count: dict[str, int] = {}

# loop through the students and count the number of students in each major
for student in students:
    # get the major of the student
    major = student["Major"]
    # increment the count of the major
    major_count[major] = major_count.get(major, 0) + 1

# print the count of students in each major
print("\n--- Students per Major ---")
# loop through the major_count dictionary and print the major and the count
for major, count in major_count.items():
    print(f"{major}: {count}")


# -------------------------------------------------
# Task 7 - Print students with GPA 3.5 or higher
# -------------------------------------------------
print("\n--- Students with GPA >= 3.5 ---")
for student in students:
    # print the students with GPA 3.5 or higher
    if float(student["GPA"]) >= 3.5:
        print(student["Name"])


# -------------------------------------------------
# Stretch challenge - Write a summary to a file
# -------------------------------------------------
# calculate the total GPA of the students
total_gpa = sum(float(s["GPA"]) for s in students)

# calculate the number of students
num_students = len(students)

# calculate the average GPA of the students
average_gpa = total_gpa / num_students
print(f"\nAverage GPA: {average_gpa:.2f}")

# print the students older than 21
print("\n--- Students older than 21 ---")
# loop through the students and print the students older than 21
for student in students:
    # print the students older than 21
    if int(student["Age"]) > 21:
        print(student["Name"])

# open the summary file and write the summary
with SUMMARY_PATH.open(mode="w", encoding="utf-8") as summary_file:
    # write the summary to the summary file
    summary_file.write("Lab 2 Summary\n")
    # write the separator to the summary file
    summary_file.write("-----------------\n")
    # write the average age to the summary file
    summary_file.write(f"Average Age: {average_age:.1f}\n")
    # write the average GPA to the summary file
    summary_file.write(f"Average GPA: {average_gpa:.2f}\n")
    # write the students older than 21 to the summary file
    summary_file.write("Students older than 21:\n")
    # loop through the students and write the students older than 21 to the summary file
    for student in students:
        # write the students older than 21 to the summary file
        if int(student["Age"]) > 21:
            summary_file.write(f"- {student['Name']}\n")

# print the summary written to the summary file
print(f"\nSummary written to {SUMMARY_PATH.name}")
