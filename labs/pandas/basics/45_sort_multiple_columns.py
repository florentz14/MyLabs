# ------------------------------------------------------------ #
# File: sort_multiple_columns.py
# Date: 2026-04-01
# Author: Florentino
# Description: Sorting the DataFrame by multiple columns.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df_sort_multiple_columns = pd.read_csv(IN_CSV, index_col="label")

    print("Original rows:")
    print(df_sort_multiple_columns)
    print("\nSort the data frame first by 'name' in descending order, then by 'score' in ascending order:")
    result = df_sort_multiple_columns.sort_values(by=["name", "score"], ascending=[False, True])
    print(result)


if __name__ == "__main__":
    main()
