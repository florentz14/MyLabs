# ------------------------------------------------------------ #
# File: first_three_rows.py
# Date: 2026-04-01
# Author: Florentino
# Description: Load exam_data.csv and select the first three rows.
# Explanation: It explains load exam_data.csv and select the first three rows and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")
    print("First three rows of the data frame:")
    print(df.head(3))


if __name__ == "__main__":
    main()
