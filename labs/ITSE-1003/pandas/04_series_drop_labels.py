import numpy as np
import pandas as pd


ser = pd.Series(np.arange(4.0), index=["red", "blue", "yellow", "white"])
print("Original series:")
print(ser)
print()

print("Drop one label ('yellow'):")
print(ser.drop("yellow"))
print()

print("Drop multiple labels (['blue', 'white']):")
print(ser.drop(["blue", "white"]))
