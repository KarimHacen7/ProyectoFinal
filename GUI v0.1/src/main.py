import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QResizeEvent
'''
TODO:


# MIRA ESTO https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#sphx-glr-users-explain-axes-axes-ticks-py

    HAY QUE HACER TODA LA GILADA DE LOS CANALES PARA EL CANAL ANALOGICO DIOSSSS

    Poner un buscador de flancos de subida y de bajada por canal


    CORREGIR EJE DE TIEMPO, VALORES Y EL MARGEN DE LA IZQUIERDA

    correct margins for scrollbar

    Cambiar la paleta de colores por una oscura
    

    cambiar procesado de cursores cuando no se encuentran dos flancos
    
    Preprocess flancos en todos los canales
    
    USE BLITTING WHERE APPLICABLE for cursors

DOING:

HOTFIX:
    PROGRAM BREAKS IF CURSORS ARE USED EXCESIVELLY
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