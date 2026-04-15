# ------------------------------------------------------------ #
# File: iloc.py
# Date: 2026-04-01
# Author: Florentino
# Description: Select rows/columns by integer position (iloc).
# Explanation: It explains select rows/columns by integer position and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.iloc[0])


if __name__ == "__main__":
    main()
