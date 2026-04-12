# ------------------------------------------------------------ #
# File: clean_wrong_format.py
# Date: 2026-04-12
# Author: Florentino
# Description: Cleaning track — fix bad types (dates, numbers with text).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "hospital_patients_dirty.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    print("Raw admission_date (mixed / invalid):")
    print(df["admission_date"].head(6))

    df["admission_date"] = pd.to_datetime(df["admission_date"], errors="coerce")
    df["height_cm"] = (
        df["height_cm"].astype(str).str.replace("cm", "", regex=False).str.strip()
    )
    df["height_cm"] = pd.to_numeric(df["height_cm"], errors="coerce")

    print("\nParsed admission_date (NaT where invalid):")
    print(df[["patient_id", "admission_date", "height_cm"]].head(8))

if __name__ == "__main__":
    main()
