# ------------------------------------------------------------ #
# File: rename.py
# Date: 2026-04-01
# Author: Florentino
# Description: Rename columns (rename).
# Explanation: It explains rename columns and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    df = df.rename(columns={"Name": "User"})
    print("First column name:", df.columns[0])


if __name__ == "__main__":
    main()
