import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:


# MIRA ESTO https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#sphx-glr-users-explain-axes-axes-ticks-py

    HAY QUE HACER TODA LA GILADA DE LOS CANALES PARA EL CANAL ANALOGICO DIOSSSS

    Poner un buscador de flancos de subida y de bajada por canal

    Cambiar la paleta de colores por una oscura

    CORREGIR EJE DE TIEMPO, VALORES Y EL MARGEN DE LA IZQUIERDA

    correct margins for scrollbar

    general cleanup of boilerplate

    Preprocess flancos en todos los canales

    cambiar procesado de cursores cuando no se encuentran dos flancos
    
    USE BLITTING WHERE APPLICABLE

DOING:

    PROGRAM BREAKS IF CURSORS ARE USED EXCESIVELLY
    draw visible channels only
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