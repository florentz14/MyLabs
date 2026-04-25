import matplotlib.pyplot as plt
import numpy as np


ages = np.random.randint(18, 65, 100)

plt.hist(ages, bins=5, color="steelblue", edgecolor="yellow", alpha=0.8)
plt.title("Ages of Students", fontsize=16, fontweight="bold")
plt.xlabel("Age", fontsize=12, fontweight="bold")
plt.ylabel("Frequency", fontsize=12, fontweight="bold")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()