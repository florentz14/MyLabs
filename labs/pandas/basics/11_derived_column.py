# ------------------------------------------------------------ #
# File: derived_column.py
# Date: 2026-04-01
# Author: Florentino
# Description: Add a column from existing data (approximate birth year).
# Explanation: It explains add a column from existing data and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df

REFERENCE_YEAR = 2026


def main() -> None:
    df = sample_df()
    df["birth_year"] = REFERENCE_YEAR - df["Age"]
    print(df[["Name", "birth_year"]])


if __name__ == "__main__":
    main()
