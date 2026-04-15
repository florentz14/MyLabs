# ------------------------------------------------------------ #
# File: series_attrs.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a named Series and display key attributes.
# Explanation: It explains create a named Series and display key attributes and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    named_series = pd.Series(
        [100, 200, 300, 400, 500],
        index=["Jan", "Feb", "Mar", "Apr", "May"],
        name="Monthly Sales",
    )

    print("Named Series:")
    print(named_series)
    print()
    print(f"Name   : {named_series.name}")
    print(f"dtype  : {named_series.dtype}")
    print(f"shape  : {named_series.shape}")
    print(f"size   : {named_series.size}")
    print(f"Values : {named_series.values}")
    print(f"Index  : {named_series.index.tolist()}")


if __name__ == "__main__":
    main()
