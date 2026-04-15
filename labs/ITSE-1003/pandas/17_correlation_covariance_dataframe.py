# ------------------------------------------------------------ #
# File: 17_correlation_covariance_dataframe.py
# Date: 2026-04-15
# Author: Florentino
# Description: 17 correlation covariance dataframe script.
# Explanation: It explains 17 correlation covariance dataframe script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import pandas as pd


frame2 = pd.DataFrame(
    [[1, 4, 3, 6], [4, 5, 6, 1], [3, 3, 1, 5], [4, 1, 6, 4]],
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

print("frame2:")
print(frame2)
print()

print("frame2.corr():")
print(frame2.corr())
print()

print("frame2.cov():")
print(frame2.cov())
