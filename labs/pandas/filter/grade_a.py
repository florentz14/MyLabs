# ------------------------------------------------------------ #
# File: grade_a.py
# Date: 2026-04-12
# Author: Florentino
# Description: Filter students with grade letter A (stripped) using loc.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nFilter students with grade letter A using the loc method:")
print(df.loc[df["grade_letter"].str.strip() == "A"])
