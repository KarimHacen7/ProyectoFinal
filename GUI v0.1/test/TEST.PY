from PySide6.QtCore import Signal, QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QFrame, QPushButton, QGraphicsView
from PySide6.QtGui import QPainter, QBrush, QColor, QPen


class ResizableGraphicsView(QGraphicsView):
    resized = Signal(QSize)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Emit the custom resized signal with the new size
        self.resized.emit(event.size())


class ResizableMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QFrame()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        self.graphics_view = ResizableGraphicsView()
        layout.addWidget(self.graphics_view)

        # Connect the resize event of the graphics view to a slot method
        self.graphics_view.resized.connect(self.on_graphics_view_resized)

    def on_graphics_view_resized(self, size):
        print("Graphics View resized to:", size)


if __name__ == "__main__":
    app = QApplication([])
    window = ResizableMainWindow()
    window.show()
    app.exec()
