# ------------------------------------------------------------ #
# File: penguins_attributes_grouped_bar.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Grouped bar chart of three penguin body measurements (bill depth, bill length, flipper length) per species, with value labels above each bar.
# Explanation: Builds the groups manually by shifting bar positions with `x + width * multiplier`; ax.bar_label adds a numeric label on top of every rectangle and constrained layout keeps everything spaced.
# Data source: https://allisonhorst.github.io/palmerpenguins/
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# Categories (one *group* of bars per species).
species = ("Adelie", "Chinstrap", "Gentoo")

# Mean per attribute, aligned with `species` (one bar per attribute per species).
penguin_means = {
    "Bill Depth":     (18.35, 18.43, 14.98),
    "Bill Length":    (38.79, 48.83, 47.50),
    "Flipper Length": (189.95, 195.82, 217.19),
}

# Base x-positions (one per species). Each attribute will be drawn at
# `x + width * multiplier` to place the three bars side-by-side per species.
x = np.arange(len(species))
width = 0.25
multiplier = 0

# `layout='constrained'` lets matplotlib auto-pack the legend / labels without
# clipping; preferable to plt.tight_layout() for figures with an outer legend.
fig, ax = plt.subplots(layout="constrained")

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel("Length (mm)")
ax.set_title("Penguin attributes by species")

# Centre each species label under the *middle* bar of its group:
# the group spans x .. x + 2*width, so x + width is its centre.
ax.set_xticks(x + width, species)

# 3-column legend at the top-left so it sits nicely above the bars.
ax.legend(loc="upper left", ncols=3)

# Headroom above the tallest bar (~217 for Gentoo flipper length) so the
# value labels don't collide with the legend.
ax.set_ylim(0, 250)

plt.show()
