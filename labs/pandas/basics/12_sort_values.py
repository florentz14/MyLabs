# ------------------------------------------------------------ #
# File: sort_values.py
# Date: 2026-04-01
# Author: Florentino
# Description: Sort rows by a column (sort_values).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.sort_values(by="Score", ascending=False))


if __name__ == "__main__":
    main()
