# ------------------------------------------------------------ #
# File: groupby_mean.py
# Date: 2026-04-01
# Author: Florentino
# Description: Group by a column and take the mean of another (groupby).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.groupby("City")["Score"].mean())


if __name__ == "__main__":
    main()
