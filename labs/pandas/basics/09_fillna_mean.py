# ------------------------------------------------------------ #
# File: fillna_mean.py
# Date: 2026-04-01
# Author: Florentino
# Description: Replace NaN in a column with that column's mean.
# Explanation: It explains replace NaN in a column with that column's mean and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    # get the sample DataFrame
    df = sample_df()

    # print the DataFrame before filling NaN
    print("DataFrame before filling NaN:")
    print(df[["Name", "Score"]])
    print()
    # fill NaN with the mean of the Score column
    fillna_mean = df["Score"].mean()
    df["Score"] = df["Score"].fillna(fillna_mean)
    print()
    # print the DataFrame after filling NaN
    print("DataFrame after filling NaN:")
    print(df[["Name", "Score"]])


if __name__ == "__main__":
    main()
