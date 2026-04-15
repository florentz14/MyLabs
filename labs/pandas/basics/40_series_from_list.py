# ------------------------------------------------------------ #
# File: series_from_list.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a Series from a Python list.
# Explanation: It explains create a Series from a Python list and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    list_series = pd.Series([10, 20, 30, 40, 50])
    print("Series from a list:")
    print(list_series)


if __name__ == "__main__":
    main()
