# ------------------------------------------------------------ #
# File: people_performance_barh.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Horizontal bar chart of randomised performance scores per person, with x-error bars and value labels.
# Explanation: Uses a fixed RNG seed for reproducibility, draws barh with `xerr=`, formats each bar's value as "%.2f" via ax.bar_label, and inverts the y-axis so names read top-to-bottom.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility (date as seed: 1968-08-01).
np.random.seed(19680801)

# Categories (one bar per person) and their y-positions.
people = ("Tom", "Dick", "Harry", "Slim", "Jim")
y_pos = np.arange(len(people))

# Random performance values in [3, 13) and small per-bar error magnitudes.
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

# Horizontal bars with x-direction error bars centred on each y position.
hbars = ax.barh(y_pos, performance, xerr=error, align="center")

# Replace numeric y-ticks with people's names.
ax.set_yticks(y_pos, labels=people)

# Read labels top-to-bottom (matplotlib's default y-axis goes bottom-up).
ax.invert_yaxis()

ax.set_xlabel("Performance")
ax.set_title("How fast do you want to go today?")

# Show each bar's value, formatted to 2 decimals, at the bar's tip.
ax.bar_label(hbars, fmt="%.2f")

# Extend xlim so the labels at the bar tips are not clipped.
ax.set_xlim(right=15)

plt.tight_layout()
plt.show()
