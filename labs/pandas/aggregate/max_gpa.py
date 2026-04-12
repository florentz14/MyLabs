# ------------------------------------------------------------ #
# File: max_gpa.py
# Date: 2026-04-12
# Author: Florentino
# Description: Rows where GPA equals the column maximum.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nStudent with the highest GPA:")
print(df[df["GPA"] == df["GPA"].max()])
