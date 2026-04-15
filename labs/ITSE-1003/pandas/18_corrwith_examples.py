import pandas as pd


frame_a = pd.DataFrame(
    {
        "ball": [1, 4, 3, 6],
        "pen": [4, 5, 6, 1],
        "pencil": [3, 3, 1, 5],
        "paper": [6, 1, 5, 4],
    },
    index=["red", "blue", "yellow", "white"],
)

frame_b = pd.DataFrame(
    {
        "ball": [2, 3, 4, 5],
        "pen": [8, 2, 5, 1],
        "pencil": [1, 2, 1, 2],
        "paper": [7, 3, 4, 6],
    },
    index=["red", "blue", "yellow", "white"],
)

series_ref = pd.Series([2, 0, 4, 8], index=["red", "blue", "yellow", "white"])

print("Pairwise correlation: frame_a with frame_b (by columns)")
print(frame_a.corrwith(frame_b))
print()

print("Pairwise correlation: frame_a columns with series_ref (axis=0)")
print(frame_a.corrwith(series_ref, axis=0))
print()

print("Pairwise correlation: frame_a rows with series_ref (axis=1)")
print(frame_a.corrwith(series_ref, axis=1))
