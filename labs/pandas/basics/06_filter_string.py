# ------------------------------------------------------------ #
# File: filter_string.py
# Date: 2026-04-01
# Author: Florentino
# Description: Filter rows where a string column equals a value.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df[df["City"] == "Madrid"])


if __name__ == "__main__":
    main()
