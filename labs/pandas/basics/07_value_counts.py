# ------------------------------------------------------------ #
# File: value_counts.py
# Date: 2026-04-01
# Author: Florentino
# Description: Count unique values in a column (value_counts).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df["City"].value_counts())


if __name__ == "__main__":
    main()
