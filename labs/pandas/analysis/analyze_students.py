"""Descriptive analysis of ``data/excel/students.csv`` (majors, GPA, balances)."""

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "students.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV)
    df["enrollment_date"] = pd.to_datetime(df["enrollment_date"], errors="coerce")

    print("=" * 60)
    print("STUDENTS — overview")
    print("=" * 60)
    print(df.shape)
    print("\nNulls (note: GPA / last_login may be empty):\n", df.isna().sum().sort_values(ascending=False).head(12))

    print("\n" + "=" * 60)
    print("GPA describe (non-null)")
    print("=" * 60)
    print(df["gpa"].describe().round(3))

    print("\n" + "=" * 60)
    print("By major — count, mean GPA, total tuition balance")
    print("=" * 60)
    major = (
        df.groupby("major", dropna=False)
        .agg(
            n=("student_id", "count"),
            gpa_mean=("gpa", "mean"),
            tuition_sum=("tuition_balance", "sum"),
            scholarship_sum=("scholarship_amount", "sum"),
        )
        .sort_values("n", ascending=False)
    )
    print(major.round(2))

    print("\n" + "=" * 60)
    print("Full-time vs part-time")
    print("=" * 60)
    print(df.groupby("is_full_time", dropna=False).size())

    print("\n" + "=" * 60)
    print("Top cities by student count")
    print("=" * 60)
    print(df["city"].value_counts().head(10).to_string())


if __name__ == "__main__":
    main()
