# ------------------------------------------------------------ #
# File: cat_vs_dog_moods.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Line plot comparing cat vs. dog mood ("happy" / "bored") across six daily activities, using string values on BOTH axes.
# Explanation: Matplotlib treats string sequences as categorical and assigns each unique value an integer position internally, so plotting `activity` (x) against `dog`/`cat` mood labels (y) works directly without any manual encoding.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt

# Y-axis values per series (categorical: "bored" or "happy").
cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]

# X-axis values, shared by both series.
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig, ax = plt.subplots()

# Two line series; matplotlib places each unique mood string at its own
# y-tick and snaps the line between them as the activity changes.
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")

ax.legend()
plt.tight_layout()
plt.show()
