# ------------------------------------------------------------ #
# File: loc_age_gt20.py
# Date: 2026-04-12
# Author: Florentino
# Description: Students older than 20 using loc with a boolean mask.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nFilter students older than 20 using the loc method:")
print(df.loc[df["Age"] > 20])
