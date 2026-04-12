import pandas as pd

# step 1: create a dataset (dictionary)
data = {
    'name': ['John', 'Jane', 'Jim', 'Jill'],
    'age': [25, 30, 35, 40],
    'major': ['Computer Science', 'Mathematics', 'Physics', 'Chemistry'],
    'gpa': [3.5, 3.8, 4.0, 3.2]
}

# step 2: print the original data set
print("\nOriginal data set:")
print(data)

# step 3: create a DataFrame
df = pd.DataFrame(data)

# step 4: print the DataFrame
print("\nDataFrame:")
print(df)

# step 5: Question 1: Who is the oldest student?
print("\nWithout pandas:")
for i in range(len(data['age'])):
    if data['age'][i] > 20:
        print(data['name'][i])

# step 6: Question 2: Who is the oldest student?
print("\nWith pandas:")
oldest_student = df[df['age'] == df['age'].max()]
print(oldest_student)

# step 7: Question 3: Add a new column
df['grade'] = df['gpa'] * 10
print("\nDataFrame with new column:")
print(df)

# step 8: add new column (senior) df['senior'] = df['age'] > 20
df['senior'] = df['age'] > 20
print("\nDataFrame with new column (senior):")
print(df)

# step 9: Quick Analysis: Count by major
print("\nQuick Analysis: Count by major?")
print(df['major'].value_counts())

# step 10: Quick Analysis: Mean GPA by major
print("\nQuick Analysis: Mean GPA by major?")
print(df.groupby('major')['gpa'].mean())