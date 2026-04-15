# ------------------------------------------------------------ #
# File: drop_attempts.py
# Date: 2026-04-01
# Author: Florentino
# Description: Delete the attempts column from the DataFrame.
# Explanation: It explains delete the attempts column from the DataFrame and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")
    df = df.drop(columns=["attempts"])

    print("Delete the 'attempts' column from the data frame:")
    print(df)


if __name__ == "__main__":
    main()
