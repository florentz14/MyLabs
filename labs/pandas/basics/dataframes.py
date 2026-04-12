# ------------------------------------------------------------ #
# File: dataframes.py
# Date: 2026-04-12
# Author: Florentino
# Description: Basic track — DataFrame columns, dtypes, and selection.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "product": ["A", "B", "C"],
            "price": [9.99, 12.5, 3.0],
            "qty": [2, 1, 5],
        }
    )
    print(df)
    print("\nColumns:", df.columns.tolist())
    print("dtypes:\n", df.dtypes)
    print("\nSingle column (Series):\n", df["price"])
    print("\nRow 0 as Series:\n", df.iloc[0])


if __name__ == "__main__":
    main()
