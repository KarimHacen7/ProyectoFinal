import matplotlib.pyplot as plt

# Create some data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create the plot
plt.plot(x, y)

# Enable the grid
plt.grid(True)

# Hide the axes by setting their color to none and removing ticks
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().tick_params(which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False)

# Show the plot
plt.show()
