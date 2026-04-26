# ------------------------------------------------------------ #
# File: animal_speeds_bar.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Bar chart of animal running speeds in MPH, labelling each bar with the equivalent in km/h via a lambda formatter.
# Explanation: Demonstrates ax.bar_label with a callable `fmt=` so labels are computed (mph * 1.61) instead of just formatted, giving km/h on top of bars whose heights are still in MPH.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt

# Categories on the x-axis (one bar per animal).
animal_names = ["Lion", "Gazelle", "Cheetah"]

# Top running speed in miles per hour, aligned with `animal_names`.
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()

# Draw the bars and keep the BarContainer so we can label each rectangle.
bar_container = ax.bar(animal_names, mph_speed)

# Bundle three axis tweaks: y-axis label, title, and y-limit (80 leaves a touch
# of headroom above the fastest bar at 75 MPH).
ax.set(ylabel="speed in MPH", title="Running speeds", ylim=(0, 80))

# Callable formatter: convert each bar value (MPH) to km/h on the fly.
# 1 mph ~= 1.61 km/h, so 50 -> "80.5 km/h", 60 -> "96.6 km/h", etc.
ax.bar_label(bar_container, fmt=lambda x: f"{x * 1.61:.1f} km/h")

plt.tight_layout()
plt.show()
