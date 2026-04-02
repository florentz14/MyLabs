# ------------------------------------------------------------ #
# File: create_series.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a pandas Series with a custom index.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print(s)


if __name__ == "__main__":
    main()
