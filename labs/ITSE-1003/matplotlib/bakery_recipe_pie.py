# ------------------------------------------------------------ #
# File: bakery_recipe_pie.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Pie chart of a bakery recipe (flour, sugar, butter, berries) showing both % share and absolute grams inside each wedge, with an external legend.
# Explanation: Parses the gram amounts and ingredient names from a list of recipe strings, then uses a custom autopct lambda to label each wedge with "<pct>%\n(<g> g)" so percentages and absolutes coexist; the legend is anchored outside the axes via bbox_to_anchor.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# `aspect="equal"` keeps the pie circular even when figsize is non-square.
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Each entry is "<grams> g <ingredient>"; we'll split on whitespace below.
recipe = [
    "375 g flour",
    "75 g sugar",
    "250 g butter",
    "300 g berries",
]

# `data` -> floats (grams), `ingredients` -> last token (ingredient name).
data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    """Return a label combining percentage and the absolute count it implies.

    matplotlib's `autopct` callback receives only the percentage of each wedge,
    so we recover the absolute value by multiplying by the total mass.
    """
    absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"


# `pie` returns three lists when autopct is set: wedge patches, the slice
# labels (empty here), and the autopct text artists -- we keep `autotexts`
# to restyle them later. The stubs declare a 2-tuple-OR-3-tuple union return
# regardless of autopct, hence the type-ignore on the 3-tuple unpack.
wedges, texts, autotexts = ax.pie(  # pyright: ignore[reportAssignmentType]
    data,
    autopct=lambda pct: func(pct, data),
    textprops=dict(color="w"),
)

# Legend pinned to the right of the axes. The `bbox_to_anchor=(1, 0, 0.5, 1)`
# defines an invisible rectangle just outside the right edge; `loc="center left"`
# places the legend's left-centre against that rectangle.
ax.legend(
    wedges,
    ingredients,
    title="Ingredients",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
)

# Restyle the in-wedge labels: smaller and bold so they read well on colour.
plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.tight_layout()
plt.show()
