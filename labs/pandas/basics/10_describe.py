# ------------------------------------------------------------ #
# File: describe.py
# Date: 2026-04-01
# Author: Florentino
# Description: Summary statistics for numeric columns (describe).
# Explanation: It explains summary statistics for numeric columns and why it is useful in basic data analysis.
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
