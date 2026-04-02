# ------------------------------------------------------------ #
# File: basic_cleaning.py
# Date: 2026-04-01
# Author: Florentino
# Description: Starter cleaning — duplicates, missing numerics, from people.csv.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH


def main() -> None:
    path = EXCEL_PATH / "people.csv"
    if not path.is_file():
        raise FileNotFoundError(f"CSV not found: {path}")

    df = pd.read_csv(path)
    print("Before:", df.shape)

    df = df.drop_duplicates(subset=["name"], keep="first")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["age"] = df["age"].fillna(df["age"].median())

    print("After:", df.shape)
    print(df[["name", "age", "city"]].head())


if __name__ == "__main__":
    main()
