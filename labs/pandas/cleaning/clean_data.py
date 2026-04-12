# ------------------------------------------------------------ #
# File: clean_data.py
# Date: 2026-04-12
# Author: Florentino
# Description: Cleaning track — load messy hospital CSV and outline a pipeline.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "hospital_patients_dirty.csv"


def main() -> None:
    raw = pd.read_csv(IN_CSV, encoding="utf-8")
    print("Raw shape:", raw.shape)
    print(raw.head(3))

    df = raw.copy()
    df = df.drop_duplicates(subset=["patient_id"], keep="first")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["height_cm"] = (
        df["height_cm"]
        .astype(str)
        .str.replace("cm", "", regex=False)
        .str.strip()
    )
    df["height_cm"] = pd.to_numeric(df["height_cm"], errors="coerce")
    df["admission_date"] = pd.to_datetime(df["admission_date"], errors="coerce")

    print("\nAfter basic cleaning (dedupe, coerce age/height, parse dates):")
    print(df[["patient_id", "age", "height_cm", "admission_date"]].head(8))

if __name__ == "__main__":
    main()
