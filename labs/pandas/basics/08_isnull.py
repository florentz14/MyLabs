# ------------------------------------------------------------ #
# File: isnull.py
# Date: 2026-04-01
# Author: Florentino
# Description: Count missing values per column (isnull + sum).
# Explanation: It explains count missing values per column and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.isnull().sum())


if __name__ == "__main__":
    main()
