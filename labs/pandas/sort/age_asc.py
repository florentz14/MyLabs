# ------------------------------------------------------------ #
# File: age_asc.py
# Date: 2026-04-12
# Author: Florentino
# Description: Sort students by Age ascending.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nSort students by age in ascending order:")
print(df.sort_values(by="Age", ascending=True))
