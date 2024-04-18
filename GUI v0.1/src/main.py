import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication

'''
TODO:
    Reportar progreso en barra de progreso
    
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())