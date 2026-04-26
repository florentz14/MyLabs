# ------------------------------------------------------------ #
# File: bakery_recipe_donut.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Donut chart of a bakery recipe with each ingredient annotated by an arrow-and-box callout placed outside the ring.
# Explanation: Builds the donut with `wedgeprops=dict(width=0.5)` (so the slices have a hole), then for each wedge computes its mid-angle and uses ax.annotate with an "angle" connectionstyle to draw a leader line from the wedge to a boxed label on the side.
# ------------------------------------------------------------ #

from typing import Any

import matplotlib.pyplot as plt
import numpy as np

# `aspect="equal"` keeps the donut circular even though the figure is 6x3.
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Display strings (used as labels) and their numeric weights (used as wedge
# sizes). Note "1 egg" and "1/2 package of yeast" don't have grams in the
# label; their wedge sizes are estimated below in `data`.
recipe = [
    "225 g flour",
    "90 g sugar",
    "1 egg",
    "60 g butter",
    "100 ml milk",
    "1/2 package of yeast",
]
data = [225, 90, 50, 60, 100, 5]

# `wedgeprops=dict(width=0.5)` punches a hole through the centre, turning the
# pie into a donut. `startangle=-40` rotates the chart so labels don't crowd.
# Slice to (wedges, texts) so the unpack is unambiguous to type checkers --
# pie() returns a 3-tuple when autopct is set, a 2-tuple otherwise.
pie_result = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)
wedges, texts = pie_result[0], pie_result[1]

# White-filled box around each callout label, with a thin black border.
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)

# Shared annotation kwargs: arrow with no head, the box style above, and
# zorder=0 so arrows sit *behind* any overlapping wedges. Typed as
# dict[str, Any] so .update() on the inner arrowprops dict and the `**kw`
# spread into annotate() type-check cleanly under basedpyright.
kw: dict[str, Any] = dict(
    arrowprops=dict(arrowstyle="-"),
    bbox=bbox_props,
    zorder=0,
    va="center",
)

for i, p in enumerate(wedges):
    # Mid-angle of the wedge (in degrees) and its (x, y) on the unit circle.
    ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))

    # Right half of the pie -> label aligns left; left half -> aligns right.
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]

    # "angle" connection: leader line goes horizontally from the label, then
    # turns at `angleB` degrees toward the wedge's mid-angle.
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})

    ax.annotate(
        recipe[i],
        xy=(x, y),                                  # arrow tip on the wedge
        xytext=(1.35 * np.sign(x), 1.4 * y),        # label position outside
        horizontalalignment=horizontalalignment,
        **kw,
    )

ax.set_title("Matplotlib bakery: A donut")

plt.tight_layout()
plt.show()
