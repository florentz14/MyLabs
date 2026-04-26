# ------------------------------------------------------------ #
# File: gelato_sales_bar.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Vertical bar chart of gelato pints sold by flavor, with thousand-separator value labels on top of each bar.
# Explanation: Uses ax.set(...) to bundle ylabel/title/ylim in one call, and ax.bar_label with fmt='{:,.0f}' so each bar's count is shown as e.g. "4,000".
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt

# Categories on the x-axis (one bar per gelato flavor).
fruit_names = ["Coffee", "Salted Caramel", "Pistachio"]

# Pints sold per flavor, aligned with `fruit_names`.
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()

# Draw the bars and keep the BarContainer so we can label each rectangle.
bar_container = ax.bar(fruit_names, fruit_counts)

# Bundle three axis tweaks in a single call: y-axis label, title, and y-limit
# (8000 leaves a bit of headroom above the tallest bar at 7000).
ax.set(ylabel="pints sold", title="Gelato sales by flavor", ylim=(0, 8000))

# Format each bar's value with a thousands separator and no decimals (e.g. 4,000).
ax.bar_label(bar_container, fmt="{:,.0f}")

plt.tight_layout()
plt.show()
