# ------------------------------------------------------------ #
# File: cleaning.py
# Date: 2026-04-01
# Author: Florentino
# Description: Basic cleaning — dedupe, numeric coercion, fillna.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH


def main() -> None:
    df = pd.read_csv(EXCEL_PATH / "hospital_patients_dirty.csv")

    df = df.drop_duplicates(subset=["patient_id"])
    df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(0)

    print(df[["patient_id", "age", "city"]].head())


if __name__ == "__main__":
    main()
