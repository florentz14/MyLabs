# ------------------------------------------------------------ #
# File: loc.py
# Date: 2026-04-01
# Author: Florentino
# Description: Select by label (index/column names) with loc.
# Explanation: It explains select by label with loc and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.loc[1, "City"])


if __name__ == "__main__":
    main()
