# ------------------------------------------------------------ #
# File: likert_survey_stacked.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Horizontal 100% stacked bar chart for a 5-point Likert survey (Strongly disagree -> Strongly agree) across six questions.
# Explanation: Builds each segment by feeding `left=` (cumulative starts) and `width=` (per-category counts) to ax.barh; uses the diverging RdYlGn colormap so red marks "disagree" and green marks "agree", and picks white/dark text per segment based on background luminance.
# Source pattern: matplotlib gallery (lines_bars_and_markers / horizontal_barchart_distribution).
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# 5-point Likert response categories (column order = colormap order, red->green).
category_names = [
    "Strongly disagree",
    "Disagree",
    "Neither agree nor disagree",
    "Agree",
    "Strongly agree",
]

# Per-question response counts; each list must align with `category_names`.
results = {
    "Question 1": [10, 15, 17, 32, 26],
    "Question 2": [26, 22, 29, 10, 13],
    "Question 3": [35, 37,  7,  2, 19],
    "Question 4": [32, 11,  9, 15, 33],
    "Question 5": [21, 29,  5,  5, 40],
    "Question 6": [ 8, 19,  5, 30, 38],
}


def survey(results, category_names):
    """Render a horizontal stacked Likert chart.

    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        Every list must have the same length as ``category_names``.
    category_names : list of str
        The Likert category labels in the order they should be stacked.
    """
    labels = list(results.keys())

    # Shape: (n_questions, n_categories). Cumulative sums per row give the
    # x-position where each new segment starts (left edge of each bar).
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)

    # RdYlGn diverging colormap: red for negative answers, green for positive.
    # 0.15..0.85 trims the very pale ends so all five colours stay readable.
    category_colors = plt.colormaps["RdYlGn"](
        np.linspace(0.15, 0.85, data.shape[1])
    )

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()              # show "Question 1" at the top
    ax.xaxis.set_visible(False)    # x-axis values are implicit in the bars
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(
            labels, widths, left=starts, height=0.5,
            label=colname, color=color,
        )

        # Pick a text colour that contrasts with the segment background:
        # darker fills (low r*g*b) get white text, lighter fills get darkgrey.
        r, g, b, _ = color
        text_color = "white" if r * g * b < 0.5 else "darkgrey"
        ax.bar_label(rects, label_type="center", color=text_color)

    # Legend pinned above the plot, one column per category, so all five
    # labels fit on a single line.
    ax.legend(
        ncols=len(category_names),
        bbox_to_anchor=(0, 1),
        loc="lower left",
        fontsize="small",
    )

    return fig, ax


survey(results, category_names)
plt.show()
