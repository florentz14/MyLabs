# ------------------------------------------------------------ #
# File: penguins_above_avg_mass.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Stacked bar chart of penguins per species split into Below / Above the species' mean body mass; x-tick labels include the species mean as LaTeX-rendered $\mu$.
# Explanation: Iterates a {label: counts} dict and stacks each group with `bottom=`; mathtext in the species tick labels (e.g. "$\\mu=$3700.66g") is rendered by matplotlib's TeX-like parser without needing a full LaTeX install.
# Data source: https://allisonhorst.github.io/palmerpenguins/
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# X-axis categories. Each label uses mathtext ($...$) so the per-species mean
# body mass renders as "μ=<value>g" beneath the species name.
species = (
    "Adelie\n $\\mu=$3700.66g",
    "Chinstrap\n $\\mu=$3733.09g",
    "Gentoo\n $\\mu=5076.02g$",
)

# Counts per species, split into two groups (Below vs Above the species mean).
weight_counts = {
    "Below": np.array([70, 31, 58]),
    "Above": np.array([82, 37, 66]),
}

# Bar width applied to every bar.
width = 0.5

fig, ax = plt.subplots()

# `bottom` tracks the running stack height for each category as we add groups.
bottom = np.zeros(len(species))

for boolean, weight_count in weight_counts.items():
    ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")

plt.tight_layout()
plt.show()
