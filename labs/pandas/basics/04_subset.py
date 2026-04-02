# ------------------------------------------------------------ #
# File: subset.py
# Date: 2026-04-01
# Author: Florentino
# Description: Select multiple columns (subset of DataFrame).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df[["Name", "Score"]])


if __name__ == "__main__":
    main()
