import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [0, 10, 15, 25, 30]

plt.plot(x, y)

# labels for the x and y axes
labels = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]

# labels for the x and y axes
plt.xticks(x, labels, fontsize=10, rotation=45)

# labels for the y axis
plt.title("Weekly Sales")
plt.xlabel("Week")
plt.ylabel("Sales")

# show the grid
plt.grid(axis="y", alpha=0.3)

# set the tight layout
plt.tight_layout()

# save before show so the file is written reliably
plt.savefig("custom_xticks3.png")

plt.show()