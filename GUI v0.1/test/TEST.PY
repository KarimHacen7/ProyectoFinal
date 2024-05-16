import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget, QCheckBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

def create_matplotlib_plot():
    t = np.arange(0.0, 200.0, 0.01)
    s1 = np.sin(2 * np.pi * t)
    s2 = np.exp(-t)
    s3 = s1 * s2

    fig, axs = plt.subplots(3, 1, sharex=True)
    fig.subplots_adjust(hspace=0)

    for index, s in enumerate([s1, s2, s3]):
        axs[index].plot(t, s)
        axs[index].set_ylim(-1, 1) if index != 1 else axs[index].set_ylim(0, 1)  # Setting different y-limits for s2
        axs[index].set_ylabel("Canal " + str(index + 1))

    return fig, axs

def toggle_subplot_visibility(state, subplot):
    subplot.set_visible(state)
    plt.draw()

def main():
    app = QApplication(sys.argv)

    # Create a QGraphicsView and a QGraphicsScene
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)

    # Create a Matplotlib plot
    fig, axs = create_matplotlib_plot()

    # Create a FigureCanvas to display the Matplotlib plot
    canvas = FigureCanvas(fig)
    canvas.setGeometry(0, 0, 800, 600)  # Adjust the size as needed

    # Add the FigureCanvas to the QGraphicsScene
    scene.addWidget(canvas)

    # Create checkboxes for each plot
    checkboxes_layout = QVBoxLayout()
    checkboxes = []
    for index, ax in enumerate(axs):
        checkbox = QCheckBox("Plot " + str(index + 1))
        checkbox.setChecked(True)
        checkboxes_layout.addWidget(checkbox)
        checkboxes.append(checkbox)
        checkbox.stateChanged.connect(lambda state, a=ax: toggle_subplot_visibility(state == 2, a))

    # Create a layout to hold the QGraphicsView and checkboxes
    layout = QVBoxLayout()
    layout.addWidget(view)
    layout.addLayout(checkboxes_layout)

    # Create a widget to hold the layout
    widget = QWidget()
    widget.setLayout(layout)
    widget.setWindowTitle("Matplotlib Plot in PySide6")

    # Show the widget
    widget.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
