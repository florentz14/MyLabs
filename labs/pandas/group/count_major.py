# ------------------------------------------------------------ #
# File: count_major.py
# Date: 2026-04-12
# Author: Florentino
# Description: Group by Major and count rows (size).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nGroup students by major and count the number of students:")
print(df.groupby("Major").size())
