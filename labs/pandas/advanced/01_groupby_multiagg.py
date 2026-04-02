# ------------------------------------------------------------ #
# File: 01_groupby_multiagg.py
# Date: 2026-04-02
# Author: Florentino
# Description: Multi-key groupby with multiple aggregations.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, index_col="label")

    grouped = (
        df.groupby(["region", "passed"], dropna=False)
        .agg(
            students=("name", "count"),
            avg_score=("score", "mean"),
            median_score=("score", "median"),
            avg_hours=("study_hours", "mean"),
            total_attempts=("attempts", "sum"),
        )
        .sort_values(["region", "passed"])
    )

    print("=" * 65)
    print("GROUPBY MULTI-AGG (region, passed)")
    print("=" * 65)
    print(grouped.round(2))


if __name__ == "__main__":
    main()
