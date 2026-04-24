import matplotlib.pyplot as plt

# create a list of x values
x = [1, 2, 3, 4, 5]

# create a list of y values
y = [10, 20, 25, 30, 40]

# plot the x and y values
plt.plot(x, y)
plt.title("Simple line plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.show()