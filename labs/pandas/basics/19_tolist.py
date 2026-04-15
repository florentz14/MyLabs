# ------------------------------------------------------------ #
# File: tolist.py
# Date: 2026-04-01
# Author: Florentino
# Description: Convert a Series to a plain Python list (tolist).
# Explanation: It explains convert a Series to a plain Python list and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    names = df["Name"].tolist()
    print(names)


if __name__ == "__main__":
    main()
