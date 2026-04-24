import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [0, 10, 15, 25, 30]

plt.plot(x, y)

# custom xticks position: need one label per tick (5 positions in x / y)
plt.xticks( [1,2,3,4,5])
plt.yticks([0,10,15,25,30])

# set the title and labels
plt.title("Custom X and Y Ticks", fontsize=14, fontweight="bold")
plt.xlabel("X Axis", fontsize=12)
plt.ylabel("Y Axis", fontsize=12)

plt.show()