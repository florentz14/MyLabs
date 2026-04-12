# ------------------------------------------------------------ #
# File: analyze_data.py
# Date: 2026-04-12
# Author: Florentino
# Description: Basic track — head, info, describe, and value_counts.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    print("head():\n", df.head(3))
    print("\ninfo():")
    df.info()
    print("\ndescribe() (numeric):\n", df.describe())
    print("\nvalue_counts (region):\n", df["region"].value_counts(dropna=False))

if __name__ == "__main__":
    main()
