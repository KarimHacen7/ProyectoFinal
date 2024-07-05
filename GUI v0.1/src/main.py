import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:

    I2C Decode needs a little more love

    El decode de binario anda medio raro

DOING:
    ORDENAR TEMPORALMENTE LA TABLA DE TRAMAS
    
    CHEQUEAR QUE A VECE NO ANDA EL NO MOSTRAR SI NO ENTRA (SUCEDE AL CAMBIAR LA INTERPRETACION) (SE ARREGLA AL RESIZE EL EJE)

HOTFIX:
    extremos navigation scrollbar

    SPI, UART CAPTURE WITH TRIGGER are DISASTROUS, LOW IMPEDANCE WITH TRIGGER PROGRAM???
    Al cambiar de gatillado, se repite la orden anterior    
                                                            # Hardware noise/parasitic capacitance
                                                            # ANALOG MODE IS NOT AFFECTED BY THIS
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