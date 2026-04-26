# ------------------------------------------------------------ #
# File: categorical_three_views.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Same categorical fruit data shown three ways (bar, scatter, line) in a single 1x3 figure with a shared y-axis.
# Explanation: Demonstrates that matplotlib accepts string x-values directly (no manual encoding needed) and that `sharey=True` keeps the three panels comparable at a glance.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt

# Categorical data: fruit name -> count.
data = {"apple": 10, "orange": 15, "lemon": 5, "lime": 20}

# Split keys/values into parallel lists for the plotting calls.
names = list(data.keys())
values = list(data.values())

# 1 row, 3 columns; sharey=True so all three panels use the same y-scale and
# the visual heights are directly comparable across plots.
fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

# Same data, three different representations:
axs[0].bar(names, values)      # categorical bar chart
axs[1].scatter(names, values)  # one point per category
axs[2].plot(names, values)     # connected line (treats categories as ordered)

fig.suptitle("Categorical Plotting")
plt.tight_layout()
plt.show()
