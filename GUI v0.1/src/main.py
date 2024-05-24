import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:
    Poner UNIDADES en los MAJOR TICKS en vez del string tiempo

DOING:  
    Pause cursor with buttom or key

HOTFIX:

    triggerchannelcombobox muestra 2 veces el canal 8 en modo analogico
    Hacer invisibles los textlabel de los canales
    Cambiar comportamiento del cursor en los extremos (buscador de flancos), donde ya no se desplaza el eje, mover solo el cursor
    Al cambiar de gatillado, se repite la orden anterior    # THIS SEEMS TO BE A FIRMWARE ISSUE
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