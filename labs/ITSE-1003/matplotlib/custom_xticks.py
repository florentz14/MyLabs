import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(x, y)

# custom xticks: need one label per tick (10 positions in x / y)
plt.xticks(x, list(map(str, range(10))), fontsize=10)
plt.yticks(y, list(map(str, range(10))), fontsize=10)

# set the title and labels
plt.title("Custom X and Y Ticks", fontsize=14, fontweight="bold")
plt.xlabel("X Axis", fontsize=12)
plt.ylabel("Y Axis", fontsize=12)

plt.show()