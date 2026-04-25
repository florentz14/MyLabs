import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
STUDENTS_GRADES_DATA_PATH = DATA_PATH / "studentsG.csv"

# read the students grades data
df = pd.read_csv(STUDENTS_GRADES_DATA_PATH)

# create  category and value columns
df["category"] = pd.cut(
    df["Grade"], 
    bins=[0, 60, 70, 80, 90, 100],
    labels=["A", "B", "C", "D", "F"]
    )

# count the number of students in each category
df_count = df["category"].value_counts()

# figure size
plt.figure(figsize=(10, 10), dpi=100)

# create the pie chart
plt.pie(
    df_count, 
    labels=df_count.index.tolist(), 
    autopct="%1.1f%%",
    startangle=90,
    counterclock=False, # counterclockwise rotation
    shadow=True, # add a shadow to the pie chart
    explode=[0.1, 0.1, 0.1, 0.1, 0.1] # explode the slices
)

# add the title
plt.title("Students Grades Distribution by Category", pad=20, fontsize=15)

# add the legend
plt.legend(df_count.index.tolist(), title="Grade")

# automatically adjust the margins to avoid cutting the text
plt.tight_layout()

# show the plot
plt.show()