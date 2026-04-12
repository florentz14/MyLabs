# ------------------------------------------------------------ #
# File: min_grade.py
# Date: 2026-04-12
# Author: Florentino
# Description: Rows where grade equals the column minimum.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nStudent with the lowest grade:")
print(df[df["grade"] == df["grade"].min()])
