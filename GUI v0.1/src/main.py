import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:

    SPI Decode

    UART Decode

    I2C Decode

    simple binary decode (only change on edges)

DOING:  
    Poner doble cursor para ver o medir el delta tiempo

HOTFIX:

    Al cambiar de gatillado, se repite la orden anterior    # Firmware race condition for interrupt
                                                            # Hardware noise/parasitic capacitance
                                                            # ANALOG MODE IS NOT AFFECTED BY THIS, either is digital mode if first untriggered sampling is at or below 25mhz
'''

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    
    window = MainWindow()
    window.show()
    app.postEvent(window,QResizeEvent(window.ui.centralWidget.size(), window.ui.centralWidget.size()))

    sys.exit(app.exec())