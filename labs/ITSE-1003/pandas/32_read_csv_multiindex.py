from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "color_status_metrics.csv"
multi_index_frame = pd.read_csv(csv_path, index_col=["color", "status"])

print("read_csv(..., index_col=['color', 'status']):")
print(multi_index_frame)
