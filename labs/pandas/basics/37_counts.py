# ------------------------------------------------------------ #
# File: counts.py
# Date: 2026-04-01
# Author: Florentino
# Description: Frequency counts and percentages with value_counts.
# Explanation: It explains frequency counts and percentages with value_counts and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame({"color": ["red", "blue", "red", "green", "blue", "red"]})

    print("Counts:")
    print(df["color"].value_counts())

    print("\nPercentages:")
    print(df["color"].value_counts(normalize=True))

    print("\nCounts including NaN:")
    print(df["color"].value_counts(dropna=False))


if __name__ == "__main__":
    main()
