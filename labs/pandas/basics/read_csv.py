# ------------------------------------------------------------ #
# File: read_csv.py
# Date: 2026-04-12
# Author: Florentino
# Description: Basic track — load a CSV into a DataFrame (repo data/excel).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "customers.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(IN_CSV)
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    print(f"Loaded: {IN_CSV}")
    print(df.head())
    print("Shape:", df.shape)

if __name__ == "__main__":
    main()
