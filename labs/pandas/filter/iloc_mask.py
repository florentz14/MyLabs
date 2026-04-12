# ------------------------------------------------------------ #
# File: iloc_mask.py
# Date: 2026-04-12
# Author: Florentino
# Description: Rows where Age > 20 via iloc and mask nonzero indices.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import ITSE_STUDENTS_CSV, load_students

IN_CSV = ITSE_STUDENTS_CSV

df = load_students()
print("\nFilter students older than 20 using the iloc method:")
print(df.iloc[(df["Age"] > 20).to_numpy().nonzero()[0]])
