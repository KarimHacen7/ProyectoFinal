import matplotlib.pyplot as plt

# Function to create a plot with text and demonstrate getting the axes object from the text object
def plot_signal_with_text_and_get_axes(signal, x_limits, text, text_position):
    fig, ax = plt.subplots()
    ax.plot(signal)
    ax.set_xlim(x_limits)
    
    text_obj = ax.text(*text_position, text, fontsize=12, ha='center')

    # Get the axes object from the text object using the 'axes' attribute
    axes_from_text = text_obj.axes

    # Verify that the axes object from the text is the same as the original axes
    if axes_from_text == ax:
        print("Successfully retrieved the axes object from the text object")
    else:
        print("Failed to retrieve the correct axes object from the text object")
    
    plt.show()

# Example usage
signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_limits = (2, 8)
text = "Sample Text"
text_position = (5, 6)  # x, y position in data coordinates

plot_signal_with_text_and_get_axes(signal, x_limits, text, text_position)
