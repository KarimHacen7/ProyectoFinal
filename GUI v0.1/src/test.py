import matplotlib.pyplot as plt

# Create empty lists for x and y values
x_values = []
y_values = []

plt.figure(figsize=(10, 0.4), layout='constrained')

# Plot an empty line with no y-values
plt.plot(x_values, y_values)

# Set x-axis limits
plt.xlim(0, 100)
plt.ylim(0, 0.1)


# Hide y-axis
plt.gca().axes.get_yaxis().set_visible(False)

plt.tick_params(axis='x', which='both', bottom=False, top=True, labelbottom=False, labeltop=True)


# Remove the frame (hide all spines)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)


plt.gcf().set_size_inches(8, 4)

# Show the plot
plt.show()

