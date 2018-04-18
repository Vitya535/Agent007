from PyQt5.QtWidgets import QMainWindow, QPushButton
from random import randint
from FieldCell import FieldCell
from Player import Player
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
        CounterOfMines, k = 0, 1
        self.Field = []
        Cell = Player.inst("Игрок", MainWindow)
        Cell.resize(40, 40)
        Cell.move(40, 40)
        Cell.show()
        self.Field.append(Cell)
        for i in range(Width):
            for j in range(k, Height):
                R = randint(1, 7)
                W = randint(1, 5)
                Cell = FieldCell(W, MainWindow)
                if R == 1 and CounterOfMines < MinesCount:
                    Cell = Mine("Мина", MainWindow)  # Вместо этого вставить изображения
                    CounterOfMines+=1
                else:
                    Cell.clicked.connect(Player.player.move)
                Cell.resize(40,40)
                Cell.move(40*(i+1), 40*(j+1))
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

