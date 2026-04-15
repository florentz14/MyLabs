# ------------------------------------------------------------ #
# File: read_csv.py
# Date: 2026-04-01
# Author: Florentino
# Description: Read a CSV into a DataFrame and export a copy.
# Explanation: It explains read a CSV into a DataFrame and export a copy and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH, EXPORT_PATH

IN_CSV = CSV_PATH / "customers.csv"
OUT_CSV = EXPORT_PATH / "customers_copy.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, encoding="utf-8")

    print("Loaded DataFrame:")
    print(df.head())
    print("\nColumns:", df.columns.tolist())
    print("Shape:", df.shape)

    df.to_csv(OUT_CSV, index=False)
    print(f"\nExported DataFrame to: {OUT_CSV}")


if __name__ == "__main__":
    main()
