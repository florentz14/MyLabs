# ------------------------------------------------------------ #
# File: people_summary.py
# Date: 2026-04-01
# Author: Florentino
# Description: Descriptive stats — mean, median, value_counts.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "people.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV)

    print("Mean age:", round(df["age"].mean(), 2))
    print("Median salary:", round(df["salary"].median(), 2))
    print("Department counts:")
    print(df["department"].value_counts().head())

if __name__ == "__main__":
    main()
