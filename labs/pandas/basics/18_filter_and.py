# ------------------------------------------------------------ #
# File: filter_and.py
# Date: 2026-04-01
# Author: Florentino
# Description: Combine boolean conditions with & (parentheses required).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df[(df["City"] == "Madrid") & (df["Age"] > 20)])


if __name__ == "__main__":
    main()
