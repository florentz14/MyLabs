# ------------------------------------------------------------ #
# File: 12_sorting_dataframe_index_axes.py
# Date: 2026-04-15
# Author: Florentino
# Description: 12 sorting dataframe index axes script.
# Explanation: It explains 12 sorting dataframe index axes script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

print("Original DataFrame:")
print(frame)
print()

print("frame.sort_index()  # sort rows by index labels")
print(frame.sort_index())
print()

print("frame.sort_index(axis=1)  # sort columns by labels")
print(frame.sort_index(axis=1))
