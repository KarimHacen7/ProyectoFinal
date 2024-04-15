import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication


'''
TODO:
    ARREGLAR LOS PUTOS CARTELES DE ESTADO
    Optimizar WQL Query, pedir menos cosas
'''

def cleanup():
    window.quitAppEvent.set()
    window.deviceCheckThread.join()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.aboutToQuit.connect(cleanup)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())