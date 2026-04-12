# ------------------------------------------------------------ #
# File: correlations.py
# Date: 2026-04-12
# Author: Florentino
# Description: Advanced track — pairwise correlations on numeric exam columns.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    numeric = df.select_dtypes(include="number")
    print("Numeric columns:", numeric.columns.tolist())
    print("\nCorrelation matrix (Pearson):")
    print(numeric.corr(numeric_only=True).round(3))

if __name__ == "__main__":
    main()
