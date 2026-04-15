# ------------------------------------------------------------ #
# File: statistics.py
# Date: 2026-04-01
# Author: Florentino
# Description: Compute basic statistics on DataFrames.
# Explanation: It explains compute basic statistics on DataFrames and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame({"value": [10, 20, 30, 40, 50], "other": [1, 2, 3, 4, 5]})

    print("Mean:", df["value"].mean())
    print("Median:", df["value"].median())
    print("Std dev:", df["value"].std())
    print("Min:", df["value"].min())
    print("Max:", df["value"].max())
    print("Quantile 0.5 (median):", df["value"].quantile(0.5))

    print("\nCorrelation matrix:\n", df.corr())


if __name__ == "__main__":
    main()
