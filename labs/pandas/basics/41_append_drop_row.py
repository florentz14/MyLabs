# ------------------------------------------------------------ #
# File: append_drop_row.py
# Date: 2026-04-01
# Author: Florentino
# Description: Append a row, then drop it again.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")

    print("Append a new row:")
    df.loc["k"] = {
        "name": "Suresh",
        "last_name": "Gomez",
        "score": 15.5,
        "attempts": 1,
        "qualify": "yes",
        "region": "Americas",
        "country": "Mexico",
        "age": 23,
        "study_hours": 4.0,
        "passed": "yes",
        "letter_grade": "B",
        "exam_date": "2025-03-15",
        "online_exam": "yes",
        "bonus_points": 0.0,
        "campus": "North Campus",
        "attendance_pct": 95.0,
        "retake_count": 0,
        "scholarship_active": "no",
        "notes": "Inserted row demo",
    }
    print("\nPrint all records after inserting a new record:")
    print(df)

    print("\nDelete the new row and display the original rows:")
    df = df.drop("k")
    print(df)


if __name__ == "__main__":
    main()
