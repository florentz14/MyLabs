# ------------------------------------------------------------ #
# File: 21_dropna_dataframe.py
# Date: 2026-04-15
# Author: Florentino
# Description: 21 dropna dataframe script.
# Explanation: It explains 21 dropna dataframe script and why it is useful in basic data analysis.
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

print("frame3.dropna():")
print(frame3.dropna())
print()

print("frame3.dropna(how='all'):")
print(frame3.dropna(how="all"))
