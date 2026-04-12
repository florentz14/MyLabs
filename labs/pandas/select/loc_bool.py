# ------------------------------------------------------------ #
# File: loc_bool.py
# Date: 2026-04-12
# Author: Florentino
# Description: Select rows with loc and a boolean condition (Age > 30).
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nSelect rows using the loc method:")
print(df.loc[df["Age"] > 30])
