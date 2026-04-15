# ------------------------------------------------------------ #
# File: explore.py
# Date: 2026-04-01
# Author: Florentino
# Description: Explore a DataFrame with head, tail, info, describe, dtypes, and value_counts.
# Explanation: It explains explore a DataFrame with head, tail, info, describe, dtypes, and value_counts and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Anna", "Louis", "Mary", "Peter", "Sara"],
            "age": [25, 30, 28, 35, 22],
            "city": ["Madrid", "Barcelona", "Madrid", "Valencia", "Barcelona"],
        }
    )

    print("First 3 rows (head):")
    print(df.head(3))

    print("\nLast 2 rows (tail):")
    print(df.tail(2))

    print("\nShape:", df.shape)

    print("\nColumn info:")
    df.info()

    print("\nDtypes:")
    print(df.dtypes)

    print("\nStatistics (describe):")
    print(df.describe())

    print("\nUnique city values:", df["city"].unique().tolist())

    print("\nCount by city (value_counts):")
    print(df["city"].value_counts())


if __name__ == "__main__":
    main()
