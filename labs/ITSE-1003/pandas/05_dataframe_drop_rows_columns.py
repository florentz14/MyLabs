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

print("Drop rows ['blue', 'yellow']:")
print(frame.drop(["blue", "yellow"]))
print()

print("Drop columns ['pen', 'pencil'] with axis=1:")
print(frame.drop(["pen", "pencil"], axis=1))
