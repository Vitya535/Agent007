from PyQt5.QtWidgets import QPushButton, QMainWindow
from ImagesForGame import IconsForGame

class Mine(QPushButton):
    def __init__(self, i:int, j:int, MainWindow:QMainWindow):
        return super().__init__(IconsForGame.ImgMine(), "Мина", MainWindow)
        self.i = i
        self.j = j

    @property
    def get_X(self)->int:
        return self.i

    @property
    def get_Y(self)->int:
        return self.j
