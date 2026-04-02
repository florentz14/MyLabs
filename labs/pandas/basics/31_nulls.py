# ------------------------------------------------------------ #
# File: nulls.py
# Date: 2026-04-01
# Author: Florentino
# Description: Handle null values with isna, fillna, and dropna.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "a": [1, np.nan, 3, 4],
            "b": [5, 6, np.nan, 8],
            "c": [9, 10, 11, 12],
        }
    )

    print("DataFrame with nulls:\n", df)
    print("\nDetect nulls (isna):\n", df.isna())
    print("\nCount nulls per column:\n", df.isna().sum())

    df_no_nulls = df.dropna()
    print("\nNo null rows (dropna):\n", df_no_nulls)

    df_filled = df.fillna(0)
    print("\nFill with 0 (fillna):\n", df_filled)


if __name__ == "__main__":
    main()
