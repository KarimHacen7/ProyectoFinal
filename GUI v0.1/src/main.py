import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:
    Poner doble cursor para ver o medir el delta tiempo

DOING:  
    Al cambiar de gatillado, se repite la orden anterior    # THIS SEEMS TO BE A FIRMWARE ISSUE
                                                            # ANALOG MODE IS NOT AFFECTED BY THIS

HOTFIX:
    comportamiento barra scroll en los extremos
    restablecer datos de configuracion al cambiar entre analogico y digital
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