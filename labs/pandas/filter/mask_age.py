# ------------------------------------------------------------ #
# File: mask_age.py
# Date: 2026-04-12
# Author: Florentino
# Description: Filter rows with a boolean mask (Age > 30).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nSelect rows where Age is greater than 30:")
print(df[df["Age"] > 30])
