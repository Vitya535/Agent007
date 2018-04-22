from PyQt5.QtWidgets import QMainWindow
from random import randint
from FieldCell import *
from Mine import *
from Player import *

class MyGame():
    __instance = None

    @staticmethod
    def inst(Width:int, Height:int, MinesCount:int, MainWindow:QMainWindow):
        if MyGame.__instance is None:
            MyGame.__instance = MyGame(Width, Height, MinesCount, MainWindow)
        return MyGame.__instance

    def __init__(self, Width:int, Height:int, MinesCount:int, MainWindow:QMainWindow):
        self.MainWindow = MainWindow
        self.Width = Width
        self.Height = Height
        self.Field = []
        self.CountBox = Width * Height
        self.Goal = Width * Height // 4
        self.Score = 0
        CounterOfMines, k = 0, 1
        Cell = MyPlayer.inst(MainWindow)
        self.Field.append(Cell)
        for i in range(Width):
            for j in range(k, Height):
                R = randint(1, 7)
                W = randint(1, 5)
                if R == 1 and CounterOfMines < MinesCount:
                    Cell = MyMine(i, j, MainWindow)
                    CounterOfMines+=1
                else:
                    Cell = MyCell(W, i, j, MainWindow)
                self.Field.append(Cell)
            self.Field.append([])
            k = 0

    @property
    def get_width() -> int:
        return MyGame.__instance.Width

    @property
    def get_height() -> int:
        return MyGame.__instance.Height

    @property
    def get_cell(i:int, j:int):
        return MyGame.__instance.Field[i, j]

    @staticmethod
    def Count_Score_And_Boxes(Boxes:list):
        MyGame.__instance.CountBox -= len(Boxes)
        MyGame.__instance.Score += sum(Boxes) * 10
        MyGame.__instance.MainWindow.BoxesValue.setText(str(MyGame.__instance.CountBox))
        MyGame.__instance.MainWindow.ScoreValue.setText(str(MyGame.__instance.Score))

