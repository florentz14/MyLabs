# ------------------------------------------------------------ #
# File: col_status.py
# Date: 2026-04-12
# Author: Florentino
# Description: Add Status column with apply/lambda (Passed vs Failed).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
df["Status"] = df["grade"].apply(lambda x: "Passed" if x >= 70 else "Failed")
print("\nDataFrame with new column (Status):")
print(df)
