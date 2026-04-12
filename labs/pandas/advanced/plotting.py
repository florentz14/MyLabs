# ------------------------------------------------------------ #
# File: plotting.py
# Date: 2026-04-12
# Author: Florentino
# Description: Advanced track — simple matplotlib plot from a DataFrame.
# ------------------------------------------------------------ #

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from settings import CSV_PATH, EXPORT_PATH

IN_CSV = CSV_PATH / "exam_data.csv"
OUT_PNG = EXPORT_PATH / "pandas_score_vs_study_hours.png"


def main() -> None:
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    sub = df.dropna(subset=["score", "study_hours"])

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(sub["study_hours"], sub["score"], alpha=0.7)
    ax.set_xlabel("study_hours")
    ax.set_ylabel("score")
    ax.set_title("Exam score vs study hours")
    fig.tight_layout()

    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"Saved: {Path(OUT_PNG).resolve()}")

if __name__ == "__main__":
    main()
