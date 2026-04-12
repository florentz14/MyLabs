# ------------------------------------------------------------ #
# File: load_csv.py
# Date: 2026-04-12
# Author: Florentino
# Description: Load students.csv and strip column names; show shape and head.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("Loaded shape:", df.shape)
print(df.head())
