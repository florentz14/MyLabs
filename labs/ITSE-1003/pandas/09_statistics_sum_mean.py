# ------------------------------------------------------------ #
# File: 09_statistics_sum_mean.py
# Date: 2026-04-15
# Author: Florentino
# Description: 09 statistics sum mean script.
# Explanation: It explains 09 statistics sum mean script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

print("frame.sum():")
print(frame.sum())
print()

print("frame.mean():")
print(frame.mean())
