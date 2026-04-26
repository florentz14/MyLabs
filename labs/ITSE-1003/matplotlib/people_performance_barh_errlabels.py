# ------------------------------------------------------------ #
# File: people_performance_barh_errlabels.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Horizontal bar chart variant where each bar is labelled with its `+/- error` value, using custom padding, color and font size.
# Explanation: Same data + seed as people_performance_barh.py; the difference is bar_label receives an explicit `labels=` list of `±err` strings (instead of the bar value via `fmt=`) plus `padding`, `color` and `fontsize` to control look-and-feel.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility (same seed as the sibling script).
np.random.seed(19680801)

# Categories and their y-positions.
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

# Custom labels: the error magnitude with a leading ± sign, padded 8 px from
# the bar tip, in blue and 14 pt so they stand out against the axes.
ax.bar_label(
    hbars,
    labels=[f"±{e:.2f}" for e in error],
    padding=8,
    color="b",
    fontsize=14,
)

# Extend xlim a bit further than the previous variant so the larger labels fit.
ax.set_xlim(right=16)

plt.tight_layout()
plt.show()
