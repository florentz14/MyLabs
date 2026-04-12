# ------------------------------------------------------------ #
# File: col_one.py
# Date: 2026-04-12
# Author: Florentino
# Description: Select a single column by name.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nSelect one column:")
print(df["Name"])
