from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "people_basic.csv"
csvframe = pd.read_csv(csv_path)

print("csvframe:")
print(csvframe)
