# ------------------------------------------------------------ #
# File: 20_filter_dropna_series.py
# Date: 2026-04-15
# Author: Florentino
# Description: 20 filter dropna series script.
# Explanation: It explains 20 filter dropna series script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


ser = pd.Series([0, 1, 2, np.nan, 9], index=["red", "blue", "yellow", "white", "green"])

print("Original series:")
print(ser)
print()

print("ser.dropna():")
print(ser.dropna())
print()

print("ser[ser.notnull()]:")
print(ser[ser.notnull()])
