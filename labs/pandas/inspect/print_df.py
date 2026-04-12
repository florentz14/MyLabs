# ------------------------------------------------------------ #
# File: print_df.py
# Date: 2026-04-12
# Author: Florentino
# Description: Print the full students DataFrame.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nDataFrame:")
print(df)
