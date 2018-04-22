from PyQt5.QtWidgets import QPushButton, QMainWindow
from ImagesForGame import *

class MyMine(QPushButton):
    """description of class"""

    def __init__(self, i:int, j:int, MainWindow:QMainWindow):
        super().__init__(MainWindow)
        self.initMine(i, j)
        self.i, self.j = i, j

    def initMine(self, i:int, j:int):
        self.setIcon(IconsForGame.GetMine())
        self.setFixedSize(38, 38)
        self.move(38 * (i + 1), 38 * (j + 1))
        self.show()

    @property
    def get_X(self) -> int:
        return self.i

    @property
    def get_Y(self) -> int:
        return self.j


