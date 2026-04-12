# ------------------------------------------------------------ #
# File: remove_duplicates.py
# Date: 2026-04-12
# Author: Florentino
# Description: Cleaning track — drop duplicate rows (e.g. repeated patient_id).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "hospital_patients_dirty.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    print("Rows before:", len(df))
    dup_mask = df.duplicated(subset=["patient_id"], keep=False)
    print("\nDuplicate patient_id groups:")
    print(df.loc[dup_mask, ["patient_id", "full_name", "city"]])

    unique = df.drop_duplicates(subset=["patient_id"], keep="first")
    print("\nRows after drop_duplicates (keep='first'):", len(unique))

if __name__ == "__main__":
    main()
