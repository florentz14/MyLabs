import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


years = np.arange(2006, 2016)
populations = 1000000000 + years * 1000000

print(len(years))
print(len(populations))

plt.plot(years, populations, color="red", linestyle="--", marker="o",linewidth=2)
plt.title("Population Growth")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()