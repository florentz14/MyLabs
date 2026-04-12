# ------------------------------------------------------------ #
# File: head.py
# Date: 2026-04-12
# Author: Florentino
# Description: Show the first five rows with head().
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nFirst 5 rows:")
print(df.head())
