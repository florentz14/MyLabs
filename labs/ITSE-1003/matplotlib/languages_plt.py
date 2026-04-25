import matplotlib.pyplot as plt
import numpy as np

languages = np.array(["Python", "Java", "C++", "JavaScript", "Ruby"])
ratings = np.array([4.5, 4.3, 4.0, 3.8, 3.5])

plt.bar(languages, ratings, color="red", alpha=0.8, width=0.5, align="edge", edgecolor="green", linewidth=2)
plt.title("Programming Language Ratings", fontsize=16, fontweight="bold")
plt.xlabel("Language", fontsize=12, fontweight="bold")
plt.ylabel("Rating", fontsize=12, fontweight="bold")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()