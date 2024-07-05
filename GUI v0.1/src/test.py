import matplotlib.pyplot as plt

def plot_signal_with_text(signal, x_limits, text, text_position):
    fig, ax = plt.subplots()
    ax.plot(signal)
    ax.set_xlim(x_limits)
    
    text_obj = ax.text(*text_position, text, fontsize=12, ha='center')

    # Draw the plot to calculate text positions
    fig.canvas.draw()

    # Get the bounding box of the text in display coordinates
    bbox = text_obj.get_window_extent(renderer=fig.canvas.get_renderer())

    # Convert display coordinates to data coordinates
    bbox_data_coords = ax.transData.inverted().transform(bbox)

    # Determine if the text is within the x limits of the plot
    x_data_min, y_data_min = bbox_data_coords[0]
    x_data_max, y_data_max = bbox_data_coords[1]

    print("x min: %s" %x_data_min)
    print("x max: %s" %x_data_max)
    print("y min: %s" %y_data_min)
    print("y max: %s" %y_data_max)
    
    plt.show()

# Example usage
signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_limits = (2, 8)
text = "Sample Text"
text_position = (5, 6)  # x, y position in data coordinates

#plot_signal_with_text(signal, x_limits, text, text_position)

if 0:
    print("Asd")