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
    df = sample_df()
    print(df.describe())


if __name__ == "__main__":
    main()
