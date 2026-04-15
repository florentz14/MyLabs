# ------------------------------------------------------------ #
# File: getting_started.py
# Date: 2026-04-12
# Author: Florentino
# Description: Basic track — import, Series, and a small DataFrame.
# Explanation: It explains basic track — import, Series, and a small DataFrame and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    # Typical install: pip install pandas
    scores = pd.Series([88, 92, 76], index=["Ana", "Luis", "Mia"], name="score")
    print("Series:")
    print(scores)

    roster = pd.DataFrame(
        {
            "name": ["Ana", "Luis"],
            "age": [20, 22],
            "major": ["CS", "Math"],
        }
    )
    print("\nDataFrame:")
    print(roster)
    print("\nShape:", roster.shape)


if __name__ == "__main__":
    main()
