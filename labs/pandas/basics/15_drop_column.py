# ------------------------------------------------------------ #
# File: drop_column.py
# Date: 2026-04-01
# Author: Florentino
# Description: Remove a column (drop).
# Explanation: It explains remove a column and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df

REFERENCE_YEAR = 2026


def main() -> None:
    df = sample_df()
    df["birth_year"] = REFERENCE_YEAR - df["Age"]
    trimmed = df.drop(columns=["birth_year"])
    print(list(trimmed.columns))


if __name__ == "__main__":
    main()
