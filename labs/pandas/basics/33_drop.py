# ------------------------------------------------------------ #
# File: drop.py
# Date: 2026-04-01
# Author: Florentino
# Description: Drop rows, columns, and duplicate rows.
# Explanation: It explains drop rows, columns, and duplicate rows and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "a": [1, 2, 2, 3],
            "b": [4, 5, 5, 6],
            "c": [7, 8, 9, 10],
        }
    )

    df_no_b = df.drop(columns=["b"])
    print("Without column 'b':\n", df_no_b)

    df_no_rows = df.drop(index=[0, 1])
    print("\nWithout rows 0 and 1:\n", df_no_rows)

    df_dup = pd.DataFrame({"x": [1, 1, 2, 2], "y": [3, 3, 4, 5]})
    df_unique = df_dup.drop_duplicates()
    print("\nWithout duplicates:\n", df_unique)


if __name__ == "__main__":
    main()
