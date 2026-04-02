# ------------------------------------------------------------ #
# File: sum_attempts.py
# Date: 2026-04-01
# Author: Florentino
# Description: Sum examination attempts from exam_data.csv.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")
    print("Sum of the examination attempts by the students:")
    print(df["attempts"].sum())


if __name__ == "__main__":
    main()
