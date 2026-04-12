# ------------------------------------------------------------ #
# File: describe.py
# Date: 2026-04-01
# Author: Florentino
# Description: Summary statistics for numeric columns (describe).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    # get the sample DataFrame
    df = sample_df()

    # print the describe of the DataFrame
    print("Describe of the DataFrame:")
    print(df.describe())
    print()


if __name__ == "__main__":
    main()
