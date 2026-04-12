# ------------------------------------------------------------ #
# File: slice_rows.py
# Date: 2026-04-12
# Author: Florentino
# Description: Select rows by label slice (first three rows via [0:3]).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nSelect rows using the slice operator:")
print(df[0:3])
