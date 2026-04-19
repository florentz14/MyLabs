from pathlib import Path

import pandas as pd

# week 3 practice: load students-WEEK3.csv (messy data: duplicates, missing values, etc.)

_DATA_DIR = Path(__file__).resolve().parent / "data"

# load the data set from students-WEEK3.csv (path works no matter the cwd)
df = pd.read_csv(_DATA_DIR / "students-WEEK3.csv")

# remove the the sapces in the column names
df.columns = df.columns.str.strip()


# missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# duplicate rows: df.duplicated() compares ALL columns, so different Id => never a full duplicate
#print("\nFull-row duplicates (all columns identical, including Id):")
#print(df.duplicated().sum())

'''cols_without_id = [c for c in df.columns if c != "Id"]
print("\nDuplicates ignoring Id (same profile, different Id — clones in WEEK3):")
print(df.duplicated(subset=cols_without_id).sum())
print("Rows involved in any such duplicate (keep=False):")
print(df.duplicated(subset=cols_without_id, keep=False).sum()) '''

# unique values in each column
#print("\nUnique values in each column:")
#print(df.nunique())

# describe the data
#print("\nDescribe the data:")
#print(df.describe())

# remove rercords using dropna()
df_cleaned = df.dropna(subset=["Grade"])
print("\nData after removing rows with missing values:")
print(df_cleaned)
print("Number of rows after cleaning:", len(df_cleaned))

print("fill missign Age with the average age")
average_age = df_cleaned["Age"].mean()
print("Average age:", average_age)

df["Age"] = df["Age"].fillna(average_age)
print("\nData after filling missing Age with the average age:")
print(df)
print()

# who is the top student?
#top_student = df[df["Grade"] == df["Grade"].max()]
top_student = df.sort_values(by="Grade", ascending=False).iloc[0] # sort by Grade in descending order and get the first row
print("\nTop student:")
print(top_student)

# who is the bottom student?
bottom_student = df.sort_values(by="Grade", ascending=True).iloc[0] # sort by Grade in ascending order and get the first row
print("\nBottom student:")
print(bottom_student)

# remove duplicates using drop_duplicates()
'''df = df.drop_duplicates()
df = df[df.duplicated(subset=["Id"])]
print("\nData after removing duplicates:")
print(df)'''

# if we can see another field repeated, we can use the following code to remove the duplicates
df_no_duplicates = df.drop_duplicates(subset=["Email"])
print("\nData after removing duplicates by Email:")
print(df_no_duplicates)

# change de Id to SID (Student ID)
df_rename = df.rename(columns={"Id": "SID"})
print("\nData after renaming the Id column to SID:")
print(df_rename)

# save the data to a new csv file
df_rename.to_csv(_DATA_DIR / "students_SID.csv", index=False)
print("\nData exported to students_SID.csv")

# export to excel file
df_rename.to_excel(_DATA_DIR / "students_SID.xlsx", index=False)
print("\nData exported to students_SID.xlsx")

# export to excel using ExcelWriter
with pd.ExcelWriter(_DATA_DIR / "students_SID.xlsx") as writer:
    df_rename.to_excel(writer, sheet_name="Students", index=False)
    print("\nData exported to students_SID.xlsx")

    # get the top students and save them  in a tab on excel a new sheet
    top_students = df.sort_values(by="Grade", ascending=False)
    top_students.to_excel(writer, sheet_name="Top Students", index=False)
    print("\nTop students exported to Top Students sheet")

