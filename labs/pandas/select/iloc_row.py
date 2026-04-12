# ------------------------------------------------------------ #
# File: iloc_row.py
# Date: 2026-04-12
# Author: Florentino
# Description: Select one row by integer position with iloc.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nSelect rows using the iloc method:")
print(df.iloc[0])
