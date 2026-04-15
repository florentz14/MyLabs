# ------------------------------------------------------------ #
# File: head.py
# Date: 2026-04-01
# Author: Florentino
# Description: Show the first n rows of a DataFrame (head).
# Explanation: It explains show the first n rows of a DataFrame and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df, sample_df_large


def main() -> None:
    # print the first 2 rows of the sample DataFrame
    print("Sample DataFrame:")
    df = sample_df()
    print(df.head(2))
    
    # print the first 2 rows of the sample DataFrame large
    print("\nSample DataFrame Large:")
    df_large = sample_df_large()
    print(df_large.head(2))


if __name__ == "__main__":
    main()
