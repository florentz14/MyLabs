# ------------------------------------------------------------ #
# File: clean_wrong_data.py
# Date: 2026-04-12
# Author: Florentino
# Description: Cleaning track — fix impossible values (age, height, weight).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "hospital_patients_dirty.csv"


def main() -> None:
    df = pd.read_csv(IN_CSV, encoding="utf-8")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["height_cm"] = (
        df["height_cm"].astype(str).str.replace("cm", "", regex=False).str.strip()
    )
    df["height_cm"] = pd.to_numeric(df["height_cm"], errors="coerce")
    df["weight_kg"] = pd.to_numeric(df["weight_kg"], errors="coerce")

    print("Before rules (suspicious rows):")
    print(df.loc[(df["age"] < 0) | (df["age"] > 120) | (df["height_cm"] > 250), ["patient_id", "age", "height_cm", "weight_kg"]])

    clean = df.copy()
    clean["age"] = clean["age"].clip(lower=0, upper=120)
    clean["height_cm"] = clean["height_cm"].where(
        (clean["height_cm"] >= 50) & (clean["height_cm"] <= 250)
    )
    clean["weight_kg"] = clean["weight_kg"].where(
        (clean["weight_kg"] >= 2) & (clean["weight_kg"] <= 400)
    )

    print("\nAfter clip / range filters:")
    print(clean[["patient_id", "age", "height_cm", "weight_kg"]].head(8))

if __name__ == "__main__":
    main()
