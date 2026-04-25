import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
SCORE_DATA_PATH = DATA_PATH / "histogram.csv"

# read the score data
df = pd.read_csv(SCORE_DATA_PATH)

# plot the score data
plt.hist(df["Score"])
plt.show()