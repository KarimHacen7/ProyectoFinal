import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication

'''
TODO:
    poner algo para indicar que se esta muestreando
    proba pasar el thread de
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())