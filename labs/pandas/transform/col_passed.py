# ------------------------------------------------------------ #
# File: col_passed.py
# Date: 2026-04-12
# Author: Florentino
# Description: Add Passed column (boolean: grade >= 70).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
df["Passed"] = df["grade"] >= 70
print("\nDataFrame with new column (Passed):")
print(df)
