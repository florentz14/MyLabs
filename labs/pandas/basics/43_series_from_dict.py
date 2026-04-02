# ------------------------------------------------------------ #
# File: series_from_dict.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a Series from a Python dictionary.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    dict_data = {"a": 100, "b": 200, "c": 300, "d": 400}
    dict_series = pd.Series(dict_data)
    print("Series from a dictionary:")
    print(dict_series)


if __name__ == "__main__":
    main()
