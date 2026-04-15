# ------------------------------------------------------------ #
# File: shape.py
# Date: 2026-04-01
# Author: Florentino
# Description: Row and column count (df.shape).
# Explanation: It explains row and column count and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.shape)


if __name__ == "__main__":
    main()
