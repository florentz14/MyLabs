# ------------------------------------------------------------ #
# File: attempts_score_filter.py
# Date: 2026-04-01
# Author: Florentino
# Description: Filter rows where attempts < 2 and score > 15.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")

    print("Attempts < 2 and score > 15:")
    print(df[(df["attempts"] < 2) & (df["score"] > 15)])


if __name__ == "__main__":
    main()
