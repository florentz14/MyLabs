# ------------------------------------------------------------ #
# File: filter_numeric.py
# Date: 2026-04-01
# Author: Florentino
# Description: Boolean filter on a numeric column.
# Explanation: It explains boolean filter on a numeric column and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df[df["Age"] > 25])


if __name__ == "__main__":
    main()
