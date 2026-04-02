# ------------------------------------------------------------ #
# File: fillna_mean.py
# Date: 2026-04-01
# Author: Florentino
# Description: Replace NaN in a column with that column's mean.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    df["Score"] = df["Score"].fillna(df["Score"].mean())
    print(df["Score"])


if __name__ == "__main__":
    main()
