# ------------------------------------------------------------ #
# File: basic_project.py
# Date: 2026-04-01
# Author: Florentino
# Description: Skeleton workflow — load shared CSV, inspect, summarize.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "people.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV)
    print("1) Load:", df.shape[0], "rows,", df.shape[1], "columns")
    print("2) Peek:\n", df.head(3))
    print("3) Numeric summary:\n", df.select_dtypes(include="number").describe())

if __name__ == "__main__":
    main()
