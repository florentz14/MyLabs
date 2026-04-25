import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import seaborn as sns

DATA_PATH = Path(__file__).parent.parent / "data"
HEATMAP_DATA_PATH = DATA_PATH / "student_performance.csv"

# read the heatmap data
df = pd.read_csv(HEATMAP_DATA_PATH)

# drop the Student column
df_numeric = df.drop(columns=["Student"])

# calculate the correlation matrix
corr_matrix = df_numeric.corr()

# draw the heatmap (correlations range from -1 to 1, so use a divergent cmap)
sns.heatmap(
    corr_matrix,
    cmap="RdBu", # use a color map for the correlations (viridis, hot, coolwarm, inferno, seismic, plasma, RdBu, Blues, Reds, etc.)
    vmin=-1, # minimum value of the correlation
    vmax=1, # maximum value of the correlation
    center=0, # center of the correlation
    annot=True, # show the correlation values
    fmt=".2f", # format the correlation values
    square=True, # make the heatmap square  
    cbar_kws={"label": "Correlation"}, # add the color bar label
)

# add the title
plt.title("Seaborn Correlation Heatmap: Student Performance", pad=20, fontsize=15)

# add the x and y ticks
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns.tolist(), rotation=45, ha="right")
plt.yticks(range(len(corr_matrix.index)), corr_matrix.index.tolist(), fontsize=14, family="serif")

# automatically adjust the margins to avoid cutting the text
plt.tight_layout()

# show the plot
plt.show()