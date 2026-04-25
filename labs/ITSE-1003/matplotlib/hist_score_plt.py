import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
SCORE_DATA_PATH = DATA_PATH / "histogram.csv"

# read the score data
df = pd.read_csv(SCORE_DATA_PATH)

# figure size
plt.figure(figsize=(10, 10), dpi=100)

# plot the score data
plt.hist(
    df["Score"], 
    bins=10, 
    color="skyblue", 
    edgecolor="black", 
    alpha=0.7, 
    linewidth=1.5
)

# add the legend
plt.legend(df["Score"].unique().tolist(), title="Score", loc="upper right")

# automatically adjust the margins to avoid cutting the text
plt.tight_layout()

# grid lines
plt.grid(True, linestyle="--", alpha=0.5)

# add the title
plt.title("Score Distribution", pad=20, fontsize=15)

# add the x and y labels
plt.xlabel("Score", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# show the plot
plt.show()