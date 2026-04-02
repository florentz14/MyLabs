# ------------------------------------------------------------ #
# File: sort_multi.py
# Date: 2026-04-01
# Author: Florentino
# Description: Sort the DataFrame by multiple columns.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")

    print("Original rows:")
    print(df)
    print("\nSort by 'name' descending, then 'score' ascending:")
    result = df.sort_values(by=["name", "score"], ascending=[False, True])
    print(result)


if __name__ == "__main__":
    main()
