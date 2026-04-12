# ------------------------------------------------------------ #
# File: mean_grade_major.py
# Date: 2026-04-12
# Author: Florentino
# Description: Average grade per Major (groupby mean).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nAverage grade per major:")
print(df.groupby("Major")["grade"].mean())
