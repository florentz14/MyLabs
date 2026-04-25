import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
SALES_DATA_PATH = DATA_PATH / "2plotsatthesametime.csv"

# read the sales data
df = pd.read_csv(SALES_DATA_PATH)

# plot the sales data
plt.plot(df["Day"], df["Sales"])
plt.show()