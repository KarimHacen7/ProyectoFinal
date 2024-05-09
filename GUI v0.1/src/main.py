import sys
from GUI import MainWindow
from PySide6.QtWidgets import QApplication

'''
TODO:
    HAY QUE HACER TODA LA GILADA DE LOS CANALES PARA EL CANAL ANALOGICO DIOSSSS

    Cambiar como hacemo el responsiveness de las graficas, un timer que controle el tiempo desde el ultimo resize

    Crear un scrollbar o ver si se puede hacer algo con la rueda del mouse

    Poner un buscador de flancos de subida y de bajada por canal

    Cambiar la paleta de colores por una oscura

DOING:
    
    Crear un eje de tiempo 
    

'''

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())