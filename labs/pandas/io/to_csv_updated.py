# ------------------------------------------------------------ #
# File: to_csv_updated.py
# Date: 2026-04-12
# Author: Florentino
# Description: Add Passed and Status columns, write students_updated.csv.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, ITSE_STUDENTS_UPDATED_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV
OUT_CSV = ITSE_STUDENTS_UPDATED_CSV

df = load_students()
df["Passed"] = df["grade"] >= 70
df["Status"] = df["grade"].apply(lambda x: "Passed" if x >= 70 else "Failed")
print("\nSave the updated DataFrame to a new CSV file:")
df.to_csv(OUT_CSV, index=False)
print(f"Wrote: {OUT_CSV}")
