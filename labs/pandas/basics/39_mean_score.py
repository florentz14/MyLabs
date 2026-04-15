# ------------------------------------------------------------ #
# File: mean_score.py
# Date: 2026-04-01
# Author: Florentino
# Description: Calculate the mean of the score column from exam_data.csv.
# Explanation: It explains calculate the mean of the score column from exam_data.csv and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")
    print("Mean score in data frame:")
    print(df["score"].mean())


if __name__ == "__main__":
    main()
