from PyQt5.QtWidgets import QPushButton, QMainWindow
from ImagesForGame import *

class MyPlayer(QPushButton):
    """description of class"""

    player = None

    @staticmethod
    def inst(MainWindow:QMainWindow):
        if MyPlayer.player is None:
            MyPlayer.player = MyPlayer(MainWindow)
        return MyPlayer.player

    def __init__(self, MainWindow:QMainWindow):
        super().__init__(MainWindow)
        self.initPlayer()
        self.i, self.j = 0, 0

    def initPlayer(self):
        self.setIcon(IconsForGame.GetPlayer())
        self.setFixedSize(38, 38)
        self.move(38, 38)
        self.show()

    @property
    def get_X(self) -> int:
        return self.i

    @property
    def get_Y(self) -> int:
        return self.j

