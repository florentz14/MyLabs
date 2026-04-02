# ------------------------------------------------------------ #
# File: 03_rank_and_quantiles.py
# Date: 2026-04-02
# Author: Florentino
# Description: Rank scores and create quartile bands with qcut.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, index_col="label")

    ranked = df[["name", "last_name", "region", "score", "study_hours"]].copy()
    ranked = ranked.dropna(subset=["score"])

    ranked["score_rank_dense"] = ranked["score"].rank(
        method="dense", ascending=False
    )
    ranked["score_percentile"] = ranked["score"].rank(pct=True)
    ranked["score_quartile"] = pd.qcut(
        ranked["score"], q=4, labels=["Q1", "Q2", "Q3", "Q4"]
    )

    ranked = ranked.sort_values("score_rank_dense")

    print("=" * 65)
    print("RANK + QUANTILES (qcut)")
    print("=" * 65)
    print(ranked.round(3))

    print("\nQuartile counts:")
    print(ranked["score_quartile"].value_counts().sort_index())


if __name__ == "__main__":
    main()
