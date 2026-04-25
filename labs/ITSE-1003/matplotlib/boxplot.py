import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
BOXPLOT_DATA_PATH = DATA_PATH / "boxplot.csv"

df = pd.read_csv(BOXPLOT_DATA_PATH)

plt.figure(figsize=(10, 10), dpi=100)

# color palette
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# group salaries by department so each department gets its own box
groups = df.groupby("Department")["Salary"].apply(list)

# create a list of lists for the data and a list of labels for the x-axis
data = [list(values) for values in groups]

# create a list of labels for the x-axis (the departments)
labels = [str(name) for name in groups.index]

# plot the boxplot
plt.boxplot(
    data, 
    tick_labels=labels, 
    vert=True, 
    patch_artist=True, 
    boxprops=dict(color=colors[0]), 
    medianprops=dict(color=colors[1]), 
    whiskerprops=dict(color=colors[2]), 
    capprops=dict(color=colors[3]), 
    flierprops=dict(color=colors[4])
    )

# grid lines
plt.grid(True, linestyle="--", alpha=0.5)

# add the x and y labels
plt.xlabel("Department")
plt.ylabel("Salary")

# add the title
plt.title("Salary distribution by department")

# automatically adjust the margins to avoid cutting the text
plt.tight_layout()

# show the plot
plt.show()