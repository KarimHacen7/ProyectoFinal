import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:
    HAY QUE HACER TODA LA GILADA DE LOS CANALES PARA EL CANAL ANALOGICO DIOSSSS

    Cambiar la paleta de colores por una oscura

DOING:  

HOTFIX:
    cambiar lo que usa el buscador para determinar la posicion inicial, el centro del viewport no es lo mas efectivo

    A veces se muestra igual el Cero en el eje de tiempo

    FULL ZOOM SOMETIMES BREAKS THE AXES: UserWarning: constrained_layout not applied because axes 
sizes collapsed to zero.  Try making figure larger or axes decorations smaller.

    correct margins for scrollbar
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