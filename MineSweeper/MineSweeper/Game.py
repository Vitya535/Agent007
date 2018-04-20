from PyQt5.QtWidgets import QMainWindow
from random import randint
from FieldCell import FieldCell
from Player import *
from Mine import Mine

class Game():
    __instance = None

    @staticmethod
    def inst(Width:int, Height:int, MinesCount:int, MainWindow:QMainWindow):
        if Game.__instance is None:
            Game.__instance = Game(Width, Height, MinesCount, MainWindow)
        return Game.__instance

    def __init__(self, Width:int, Height:int, MinesCount:int, MainWindow:QMainWindow):
        self.Width = Width
        self.Height = Height
        self.Field = []
        CounterOfMines, k = 0, 1
        # Cell = Player.inst(MainWindow)
        # Cell.resize(30, 30)
        # Cell.move(30, 30)
        # Cell.show()
        # self.Field.append(Cell)
        for i in range(Width):
            for j in range(k, Height):
                R = randint(1, 7)
                W = randint(1, 5)
                Cell = FieldCell(W, i, j, MainWindow)
                if R == 1 and CounterOfMines < MinesCount:
                    Cell = Mine(i, j, MainWindow)
                    CounterOfMines+=1
                # else:
                #    Cell.clicked.connect(Player.player.move) # возможно здесь будет не работать
                Cell.resize(50,50)
                Cell.move(50*(i+1), 50*(j+1))
                Cell.show()
                self.Field.append(Cell)
            self.Field.append([])
            k = 0

    @property
    def get_width()->int:
        return Game.__instance.Width

    @property
    def get_height()->int:
        return Game.__instance.Height

    @property
    def get_cell(i:int, j:int):
        return Game.__instance.Field[i, j]

