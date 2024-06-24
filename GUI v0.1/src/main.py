import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:
    UART Decode
        Add support for reversing bit order

    I2C Decode needs a little more love

    El decode de binario anda medio raro
DOING:  
    CARTELITOS

HOTFIX:
    extremos navigation scrollbar

    SPI, UART CAPTURE WITH TRIGGER are DISASTROUS, LOW IMPEDANCE WITH TRIGGER PROGRAM???
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