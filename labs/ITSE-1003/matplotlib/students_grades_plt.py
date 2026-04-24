import matplotlib.pyplot as plt

students = ["John", "Jane", "Jim", "Jill"]
grades = [85, 90, 78, 92]

plt.bar(students, grades)
plt.title("Student Grades")
plt.xlabel("Student")
plt.ylabel("Grade")
plt.show()
