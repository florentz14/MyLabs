# ------------------------------------------------------------ #
# File: 52_column_headers.py
# Date: 2026-04-01
# Author: Florentino
# Description: Get a list of column headers from exam_data.csv.
# Explanation: It explains get a list of column headers from exam_data.csv and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")
    print(df.columns.tolist())
    print(f"List of column headers: {df.columns.tolist()}")


if __name__ == "__main__":
    main()
