# ------------------------------------------------------------ #
# File: clean_empty_cells.py
# Date: 2026-04-12
# Author: Florentino
# Description: Cleaning track — drop or fill missing values (NaN).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "hospital_patients_dirty.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    print("Null counts (sample columns):")
    print(df[["age", "gender", "discharge_date", "height_cm"]].isna().sum())

    filled = df.copy()
    filled["gender"] = filled["gender"].fillna("Unknown")
    age_num = pd.to_numeric(filled["age"], errors="coerce")
    filled["age"] = age_num.fillna(age_num.median())

    dropped = df.dropna(subset=["patient_id", "full_name"])
    print("\nRows after dropna on keys:", len(dropped))
    print("\nSample after fillna on gender + median age:")
    print(filled[["patient_id", "gender", "age"]].head(6))

if __name__ == "__main__":
    main()
