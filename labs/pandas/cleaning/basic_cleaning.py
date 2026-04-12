# ------------------------------------------------------------ #
# File: basic_cleaning.py
# Date: 2026-04-01
# Author: Florentino
# Description: Starter cleaning — duplicates, missing numerics, from people.csv.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "people.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV)
    print("Before:", df.shape)

    df = df.drop_duplicates(subset=["name"], keep="first")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["age"] = df["age"].fillna(df["age"].median())

    print("After:", df.shape)
    print(df[["name", "age", "city"]].head())

if __name__ == "__main__":
    main()
