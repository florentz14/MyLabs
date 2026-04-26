# ------------------------------------------------------------ #
# File: penguins_stacked_bar.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Stacked bar chart counting penguins by species and sex (Adelie, Chinstrap, Gentoo).
# Explanation: Iterates over a {sex: counts} dict, drawing each sex on top of the previous one with `bottom=` to stack the bars; centred labels show the per-segment count.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# Categories on the x-axis (one bar per species).
species = ("Adelie", "Chinstrap", "Gentoo")

# Per-sex counts aligned to the species tuple above.
sex_counts = {
    "Male":   np.array([73, 34, 61]),
    "Female": np.array([73, 34, 58]),
}

# Width of each bar (single value applies to every bar).
width = 0.6

fig, ax = plt.subplots()

# `bottom` tracks the running height so the next group stacks on top.
bottom = np.zeros(len(species))

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count
    # Print the count inside the centre of each segment.
    ax.bar_label(p, label_type="center")

ax.set_title("Number of penguins by sex")
ax.set_xlabel("Species")
ax.set_ylabel("Count")
ax.legend()

plt.tight_layout()
plt.show()
