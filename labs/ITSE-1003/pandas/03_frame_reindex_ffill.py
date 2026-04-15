import pandas as pd


frame = pd.DataFrame(
    {
        "colors": ["blue", "green", "yellow", "red", "white"],
        "price": [1.2, 1.0, 0.6, 0.9, 1.7],
        "object": ["ballpand", "pen", "pencil", "paper", "mug"],
    }
)

frame = frame.reindex(
    range(5),
    method="ffill",
    columns=["colors", "price", "new", "object"],
)

print("colors price new object")
print(frame)
