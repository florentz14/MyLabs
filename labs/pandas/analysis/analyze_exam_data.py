"""Descriptive analysis of ``data/excel/exam_data.csv`` (scores, regions, pass rate)."""

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "exam_data.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV)
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    print("=" * 60)
    print("EXAM DATA — rows, score missingness")
    print("=" * 60)
    print(df.shape)
    print("Score non-null:", df["score"].notna().sum(), "| null:", df["score"].isna().sum())

    print("\n" + "=" * 60)
    print("Score describe (non-null)")
    print("=" * 60)
    print(df["score"].describe().round(2))

    print("\n" + "=" * 60)
    print("By region — mean score, pass rate, n")
    print("=" * 60)
    passed_yes = df["passed"].astype(str).str.lower().eq("yes")
    reg = (
        df.assign(_pass=passed_yes)
        .groupby("region", dropna=False)
        .agg(
            n=("name", "count"),
            score_mean=("score", "mean"),
            pass_rate=("_pass", "mean"),
            study_hours_mean=("study_hours", "mean"),
        )
        .sort_values("n", ascending=False)
    )
    print(reg.round(3))

    print("\n" + "=" * 60)
    print("By passed flag — mean score / attempts")
    print("=" * 60)
    print(
        df.groupby("passed", dropna=False)
        .agg(score_mean=("score", "mean"), attempts_mean=("attempts", "mean"), n=("name", "count"))
        .round(3)
    )


if __name__ == "__main__":
    main()
