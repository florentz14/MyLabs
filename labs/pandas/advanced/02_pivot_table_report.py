# ------------------------------------------------------------ #
# File: 02_pivot_table_report.py
# Date: 2026-04-02
# Author: Florentino
# Description: Pivot table report by region and pass status.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, index_col="label")

    pivot = pd.pivot_table(
        df,
        index="region",
        columns="passed",
        values=["score", "study_hours", "attempts"],
        aggfunc={"score": "mean", "study_hours": "mean", "attempts": "sum"},
        margins=True,
        margins_name="Total",
    )

    print("=" * 65)
    print("PIVOT TABLE REPORT (region x passed)")
    print("=" * 65)
    print(pivot.round(2))


if __name__ == "__main__":
    main()
