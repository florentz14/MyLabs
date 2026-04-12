# ------------------------------------------------------------ #
# File: cols_multi.py
# Date: 2026-04-12
# Author: Florentino
# Description: Select multiple columns (Name, Age, Major).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nSelect multiple columns:")
print(df[["Name", "Age", "Major"]])
