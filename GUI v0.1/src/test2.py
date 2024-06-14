import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, marker='o')

# Annotate the point with maximum y value
max_y = max(y)
max_y_index = y.index(max_y)
max_x = x[max_y_index]

# Add a rectangle that spans from (1, 35) to (2, 40)
rect = patches.Rectangle((1, 35), 1, 5, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Add text inside the rectangle
ax.text(1.5, 37.5, 'Range: 1-2\n, 35-40', horizontalalignment='center', verticalalignment='center')

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Example of a rectangle annotation in matplotlib')

# Show the plot
plt.show()
