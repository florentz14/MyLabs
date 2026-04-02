# ------------------------------------------------------------ #
# File: iloc.py
# Date: 2026-04-01
# Author: Florentino
# Description: Select rows/columns by integer position (iloc).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df


def main() -> None:
    df = sample_df()
    print(df.iloc[0])


if __name__ == "__main__":
    main()
