"""Load ``data/json/students_records.json`` and mirror key student aggregates (vs CSV)."""

from __future__ import annotations

import pandas as pd

from settings import JSON_PATH

IN_JSON = JSON_PATH / "students_records.json"


def main() -> None:
    df = pd.read_json(IN_JSON)
    df["enrollment_date"] = pd.to_datetime(df["enrollment_date"], errors="coerce")

    print("=" * 60)
    print("JSON STUDENTS — shape")
    print("=" * 60)
    print(df.shape)
    print(df.dtypes)

    print("\n" + "=" * 60)
    print("Major counts (top 10)")
    print("=" * 60)
    print(df["major"].value_counts().head(10).to_string())

    print("\n" + "=" * 60)
    print("GPA by major (mean, non-null)")
    print("=" * 60)
    g = df.groupby("major")["gpa"].mean().sort_values(ascending=False).head(10)
    print(g.round(3).to_string())


if __name__ == "__main__":
    main()
