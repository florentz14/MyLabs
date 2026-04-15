# ------------------------------------------------------------ #
# File: from_rows.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a DataFrame from a list of dictionaries.
# Explanation: It explains create a DataFrame from a list of dictionaries and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    rows = [
        {"product": "A", "price": 10},
        {"product": "B", "price": 20},
    ]
    df = pd.DataFrame(rows)
    print(df)


if __name__ == "__main__":
    main()
