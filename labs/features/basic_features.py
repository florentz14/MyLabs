# ------------------------------------------------------------ #
# File: basic_features.py
# Date: 2026-04-01
# Author: Florentino
# Description: Starter feature ideas — string length, boolean flag, scaled numeric.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "first_name": ["Ana", "Bob"],
            "city": ["Austin", "Boston"],
            "salary": [48_000, 72_000],
        }
    )
    df["name_len"] = df["first_name"].str.len()
    df["is_high"] = df["salary"] >= 60_000
    df["salary_k"] = df["salary"] / 1000.0

    print(df)


if __name__ == "__main__":
    main()
