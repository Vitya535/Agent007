from PyQt5.QtWidgets import QPushButton, QMainWindow
import random as rnd
from FieldCell import FieldCell

class Game():
    def __init__(self, Width:int, Height:int, MinesCount:int, MainWindow:QMainWindow):
        self.Field = []
        for i in range(Width):
            for j in range(Height):
                Cell = FieldCell(str(rnd.randint(1,6)), MainWindow)
                Cell.resize(20, 20)
                Cell.move(10*i, 30*j)
                self.Field.append(Cell)
            self.Field.append([])

