# ------------------------------------------------------------ #
# File: 19_assign_nan_series.py
# Date: 2026-04-15
# Author: Florentino
# Description: 19 assign nan series script.
# Explanation: It explains 19 assign nan series script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


ser = pd.Series([0, 1, 2, np.nan, 9], index=["red", "blue", "yellow", "white", "green"])

print("Original series with np.nan:")
print(ser)
print()

ser["white"] = None

print("After ser['white'] = None (still NaN in pandas):")
print(ser)
