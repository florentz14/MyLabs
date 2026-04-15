# ------------------------------------------------------------ #
# File: 14_sorting_dataframe_values_by_columns.py
# Date: 2026-04-15
# Author: Florentino
# Description: 14 sorting dataframe values by columns script.
# Explanation: It explains 14 sorting dataframe values by columns script and why it is useful in basic data analysis.
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

# Old examples may show frame.sort_index(by='pen'); modern equivalent is sort_values(by=...).
print("frame.sort_values(by='pen'):")
print(frame.sort_values(by="pen"))
print()

print("frame.sort_values(by=['pen', 'pencil']):")
print(frame.sort_values(by=["pen", "pencil"]))
