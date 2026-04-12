# ------------------------------------------------------------ #
# File: slice_first3.py
# Date: 2026-04-12
# Author: Florentino
# Description: First three rows using slice notation [0:3].
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nFilter students older than 20 using the slice operator:")
print(df[0:3])
