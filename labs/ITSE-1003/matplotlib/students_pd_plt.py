import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
df = pd.read_csv(DATA_DIR / "studentsG.csv")

df.plot(kind="bar", x="Name", y="Grade")
plt.title("Final Grade by Student")
plt.xlabel("Student Name")
plt.ylabel("Grade")
plt.show()
