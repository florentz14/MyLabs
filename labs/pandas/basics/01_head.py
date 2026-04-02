# ------------------------------------------------------------ #
# File: head.py
# Date: 2026-04-01
# Author: Florentino
# Description: Show the first n rows of a DataFrame (head).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.head(2))


if __name__ == "__main__":
    main()
