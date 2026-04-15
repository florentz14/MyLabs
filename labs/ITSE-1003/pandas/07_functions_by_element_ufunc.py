# ------------------------------------------------------------ #
# File: 07_functions_by_element_ufunc.py
# Date: 2026-04-15
# Author: Florentino
# Description: 07 functions by element ufunc script.
# Explanation: It explains 07 functions by element ufunc script and why it is useful in basic data analysis.
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

# NumPy ufuncs work element by element on pandas objects.
print("np.sqrt(frame):")
print(np.sqrt(frame))
print()

print("np.exp(frame):")
print(np.exp(frame))
print()

print("np.sin(frame):")
print(np.sin(frame))
