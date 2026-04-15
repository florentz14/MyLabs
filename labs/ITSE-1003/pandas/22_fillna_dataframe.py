# ------------------------------------------------------------ #
# File: 22_fillna_dataframe.py
# Date: 2026-04-15
# Author: Florentino
# Description: 22 fillna dataframe script.
# Explanation: It explains 22 fillna dataframe script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


frame3 = pd.DataFrame(
    [[6, np.nan, 6], [np.nan, np.nan, np.nan], [2, np.nan, 5]],
    index=["blue", "green", "red"],
    columns=["ball", "mug", "pen"],
)

print("Original DataFrame:")
print(frame3)
print()

print("frame3.fillna(0):")
print(frame3.fillna(0))
print()

print("frame3.fillna({'ball': 1, 'mug': 0, 'pen': 99}):")
print(frame3.fillna({"ball": 1, "mug": 0, "pen": 99}))
