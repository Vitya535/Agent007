from PyQt5.QtWidgets import QMainWindow
from random import randint
from FieldCell import FieldCell

class Game():
    __instance = None

    @staticmethod
    def inst(Width:int, Height:int, MinesCount:int, MainWindow:QMainWindow):
        if Game.__instance is None:
            Game.__instance = Game(Width, Height, MinesCount, MainWindow)
        return Game.__instance

    def __init__(self, Width:int, Height:int, MinesCount:int, MainWindow:QMainWindow):
        self.Field = []
        for i in range(Width):
            for j in range(Height):
                Cell = FieldCell(str(randint(1,5)))
                Cell.setText(str(randint(1,5)))
                Cell.resize(30,30)
                Cell.move(30*(i+1), 30*(j+1))
                Cell.setParent(MainWindow)
                Cell.show()
                self.Field.append(Cell)
            self.Field.append([])

