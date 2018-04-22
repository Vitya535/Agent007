from PyQt5.QtWidgets import QPushButton, QMainWindow
from PyQt5.QtGui import QFont
from Player import *
from Utils import isClickedAroundPlayer, isBorderOfField
from Mine import *
from Game import *

class MyCell(QPushButton):
    """description of class"""

    def __init__(self, CountSteps:int, i:int, j:int, MainWindow:QMainWindow):
        super().__init__(str(CountSteps), MainWindow)
        self.CountSteps, self.i, self.j = CountSteps, i, j
        self.initFieldCell(i, j)

    def initFieldCell(self, i:int, j:int):
        self.setFixedSize(38, 38)
        self.move(38 * (i + 1), 38 * (j + 1))
        font = QFont()
        font.setPixelSize(20)
        self.setFont(font)
        self.clicked.connect(self.moveTo)
        self.show()

    @property
    def getCountOfSteps(self) -> int:
        return self.CountSteps

    @property
    def X(self) -> int:
        return self.i

    @property
    def Y(self) -> int:
        return self.j

    def moveTo(self):
        Check = isClickedAroundPlayer(MyPlayer.player, self)
        if Check:
            DifferenceOnRow, DifferenceOnColumn = MyPlayer.player.i - self.i, MyPlayer.player.j - self.j
            x, y = MyPlayer.player.i, MyPlayer.player.j
            Boxes = []
            if DifferenceOnColumn == 0:
                if DifferenceOnRow == -1 or DifferenceOnRow == 1:
                    for MyPlayer.player.i in range(x, x + (-DifferenceOnRow) * self.CountSteps, -DifferenceOnRow):
                        Cell = MyGame.get_cell(MyPlayer.player.i, MyPlayer.player.j)
                        Boxes.append(Cell)
                        if Cell is MyMine or isBorderOfField(Cell) or Cell.icon is IconsForGame.GetCross():
                            Cell.setIcon(IconsForGame.GetSkull())
                            break
                        elif Cell is MyCell:
                            Cell.setIcon(IconsForGame.GetCross())

            if -1 <= DifferenceOnRow <= 1:
                if DifferenceOnColumn == -1 or DifferenceOnColumn == 1:
                    for MyPlayer.player.j in range(y, y + (-DifferenceOnColumn) * self.CountSteps, -DifferenceOnColumn):
                        MyPlayer.player.i -= DifferenceOnRow
                        Cell = MyGame.get_cell(MyPlayer.player.i, MyPlayer.player.j)
                        Boxes.append(Cell)
                        if Cell is MyMine or isBorderOfField(Cell) or Cell.icon is IconsForGame.GetCross():
                            Cell.setIcon(IconsForGame.GetSkull())
                            break
                        elif Cell is MyCell:
                            Cell.setIcon(IconsForGame.GetCross())
        MyGame.Count_Score_And_Boxes(Boxes)