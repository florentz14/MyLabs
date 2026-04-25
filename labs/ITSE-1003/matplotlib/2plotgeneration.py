import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "data"
TWO_PLOTS_DATA_PATH = DATA_PATH / "2plotsatthesametime.csv"

df = pd.read_csv(TWO_PLOTS_DATA_PATH)

plt.figure(figsize=(18, 5), dpi=100)

# left subplot: daily evolution of sales, profit and expenses
plt.subplot(1, 3, 1)
plt.plot(df["Day"], df["Sales"], marker="o", label="Sales")
plt.plot(df["Day"], df["Profit"], marker="s", label="Profit")
plt.plot(df["Day"], df["Expenses"], marker="^", label="Expenses")
plt.xlabel("Day", fontsize=12)
plt.ylabel("Amount", fontsize=12)
plt.title("Daily sales, profit and expenses", pad=15, fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# pre-compute totals per category, used by the bar and pie subplots
totals_by_category = df.groupby("Category")["Sales"].sum().sort_index()
categories = [str(name) for name in totals_by_category.index]
totals = [int(value) for value in totals_by_category.values]
colors = ["#4c72b0", "#dd8452", "#55a467"]

# middle subplot: total sales per category as a bar chart
plt.subplot(1, 3, 2)
plt.bar(categories, totals, color=colors, edgecolor="black")
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total sales", fontsize=12)
plt.title("Total sales per category", pad=15, fontsize=14)
plt.grid(True, axis="y", linestyle="--", alpha=0.5)

# right subplot: same totals as a pie chart (share of each category)
plt.subplot(1, 3, 3)
plt.pie(totals, labels=categories, autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("Sales share per category", pad=15, fontsize=14)
plt.axis("equal")

plt.tight_layout()
plt.show()
