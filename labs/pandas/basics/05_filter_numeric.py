# ------------------------------------------------------------ #
# File: filter_numeric.py
# Date: 2026-04-01
# Author: Florentino
# Description: Boolean filter on a numeric column.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df[df["Age"] > 25])


if __name__ == "__main__":
    main()
