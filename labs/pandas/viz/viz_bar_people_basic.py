# ------------------------------------------------------------ #
# File: viz_bar_people_basic.py
# Date: 2026-03-29
# Author: Florentino
# Description: Small bar chart of ages from people.csv (same data as io/read_people.py).
# ------------------------------------------------------------ #

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "people.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV)

    # Create a single panel, figure handle intentionally unused
    _, ax = plt.subplots(figsize=(6, 4))

    # Plot the bar chart with the given parameters
    ax.bar(df["name"], df["age"], color="steelblue", edgecolor="navy", linewidth=0.6)
    ax.set_ylabel("Age")
    ax.set_xlabel("Name")
    ax.set_title("Age by person (people.csv)")

    # Set the y-axis limit to a small gap above the tallest bar
    ax.set_ylim(0, max(df["age"]) * 1.15)

    # Draw the numeric value on top of each bar
    for i, (name, age) in enumerate(zip(df["name"], df["age"], strict=True)):
        # Draw the numeric value on top of each bar
        ax.annotate(str(age), xy=(i, age), ha="center", va="bottom", fontsize=10)

    # Fit the labels within the figure bounds by calling tight_layout()
    plt.tight_layout()

    # Show the plot by calling show()
    plt.show()
