"""Descriptive analysis of ``data/excel/people.csv`` (salary, department, city)."""

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "people.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, parse_dates=["signup_date"])

    print("=" * 60)
    print("PEOPLE — shape, dtypes, missing")
    print("=" * 60)
    print(df.shape)
    print(df.dtypes)
    print("\nNulls per column:\n", df.isna().sum())

    print("\n" + "=" * 60)
    print("Numeric describe")
    print("=" * 60)
    print(df[["age", "salary"]].describe().round(2))

    print("\n" + "=" * 60)
    print("By department — count, mean salary")
    print("=" * 60)
    dept = (
        df.groupby("department", dropna=False)
        .agg(rows=("name", "count"), mean_salary=("salary", "mean"), median_age=("age", "median"))
        .sort_values("mean_salary", ascending=False)
    )
    print(dept.round(2))

    print("\n" + "=" * 60)
    print("By city — head (top 8 by count)")
    print("=" * 60)
    city = df.groupby("city", dropna=False).size().sort_values(ascending=False).head(8)
    print(city.to_string())

    print("\n" + "=" * 60)
    print("Active flag")
    print("=" * 60)
    print(df["is_active"].value_counts(dropna=False))


if __name__ == "__main__":
    main()
