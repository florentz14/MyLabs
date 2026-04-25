import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
BOXPLOT_DATA_PATH = DATA_PATH / "boxplot.csv"

df = pd.read_csv(BOXPLOT_DATA_PATH)

plt.figure(figsize=(10, 6), dpi=100)

# group salaries by department: one list of salaries per department
grouped = df.groupby("Department")["Salary"].apply(list)

# create a list of salaries per department
salaries_per_department = [list(values) for values in grouped]

# create a list of departments
departments = [str(name) for name in grouped.index]

# boxplot: one box per department
plt.boxplot(
    salaries_per_department, # list of salaries per department
    tick_labels=departments, # labels for the x-axis
    vert=True, # vertical boxplot
    patch_artist=True, # fill the boxes with color
)
# add the x and y labels
plt.xlabel("Department", fontsize=12)
plt.ylabel("Salary", fontsize=12)

# add the title
plt.title("Salary distribution per department", pad=20, fontsize=15)

# grid lines
plt.grid(True, axis="y", linestyle="--", alpha=0.5)

# tight layout
plt.tight_layout()

# show the plot
plt.show()