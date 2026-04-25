import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
HEATMAP_DATA_PATH = DATA_PATH / "student_performance.csv"

# read the heatmap data
df = pd.read_csv(HEATMAP_DATA_PATH)

# drop the Student column
df_numeric = df.drop(columns=["Student"])

# calculate the correlation matrix
corr_matrix = df_numeric.corr()

# print the correlation matrix
#print(corr_matrix)

# define the size of the figure 
plt.figure(figsize=(12, 6))

# draw the heatmap 
plt.imshow(corr_matrix, cmap="hot", aspect="auto")

# customization of X Ticks (Subjects)
plt.xticks(
    range(len(corr_matrix.columns)), # range of the columns
    corr_matrix.columns.tolist(), # list of the columns
    rotation=45, 
    ha="right",             # horizontal alignment of the text
    fontsize=12,            # text size
    color="darkblue",       # text color
    fontweight="bold"       # bold text
)

# customization of Y Ticks (Students)
plt.yticks(
    range(len(corr_matrix.index)), 
    corr_matrix.index.tolist(),
    fontsize=10,
    family="serif"         # change the font type
)

# configuration of the small graduation lines
plt.tick_params(axis='both', which='major', labelsize=10, width=2, length=5)

# add the title
plt.title("Correlation Heatmap: Student Performance", pad=20, fontsize=15)

# add the color bar
plt.colorbar(label="Score")

# automatically adjust the margins to avoid cutting the text
plt.tight_layout() 

# show the plot 
plt.show()