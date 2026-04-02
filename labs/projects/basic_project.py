# ------------------------------------------------------------ #
# File: basic_project.py
# Date: 2026-04-01
# Author: Florentino
# Description: Skeleton workflow — load shared CSV, inspect, summarize.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH


def main() -> None:
    path = EXCEL_PATH / "people.csv"
    if not path.is_file():
        raise FileNotFoundError(f"CSV not found: {path}")

    df = pd.read_csv(path)
    print("1) Load:", df.shape[0], "rows,", df.shape[1], "columns")
    print("2) Peek:\n", df.head(3))
    print("3) Numeric summary:\n", df.describe(numeric_only=True))


if __name__ == "__main__":
    main()
