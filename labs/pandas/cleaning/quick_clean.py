# ------------------------------------------------------------ #
# File: quick_clean.py
# Date: 2026-04-01
# Author: Florentino
# Description: Basic cleaning — dedupe, numeric coercion, fillna.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "hospital_patients_dirty.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV)

    df = df.drop_duplicates(subset=["patient_id"])
    df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(0)

    print(df[["patient_id", "age", "city"]].head())

if __name__ == "__main__":
    main()
