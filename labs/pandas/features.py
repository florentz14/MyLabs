# ------------------------------------------------------------ #
# File: features.py
# Date: 2026-04-01
# Author: Florentino
# Description: Simple derived columns — boolean flag and scaled numeric.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH


def main() -> None:
    df = pd.read_csv(EXCEL_PATH / "people.csv")

    df["is_senior"] = df["age"] >= 30
    df["salary_k"] = df["salary"] / 1000

    print(df[["name", "age", "is_senior", "salary_k"]].head())


if __name__ == "__main__":
    main()
