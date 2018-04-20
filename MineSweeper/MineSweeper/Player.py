from PyQt5.QtWidgets import QPushButton, QMainWindow
from ImagesForGame import IconsForGame
from FieldCell import FieldCell
from Utils import *
from Game import *
from Mine import Mine

class Player(QPushButton):
    player = None

    @staticmethod
    def inst(MainWindow:QMainWindow):
        if Player.player is None:
            Player.player = Player(MainWindow)
        return Player.player

    def __init__(self, MainWindow:QMainWindow):
        return super().__init__(IconsForGame.ImgPlayer(), "Игрок", MainWindow)
        self.i, self.j = 0, 0

    @property
    def get_X()->int:
        return Player.player.i

    @property
    def get_Y()->int:
        return Player.player.j

    @classmethod
    def move(self, cell:FieldCell):
        Check, DifferenceOnRow, DifferenceOnColumn = isClickedAroundPlayer(cell)
        if Check:
            for self.i, self.j in range(cell.CountSteps, [DifferenceOnRow, DifferenceOnColumn]):
                C = FieldCell(Game.get_cell[i, j])
                if Game.get_cell[i, j] is Mine or (isBorderOfField(cell) or C.CountSteps != 0):
                    cell.setIcon(IconsForGame.ImgSkull()) # нарисовать иконку черепа (там где игрок погиб)
                elif Game.get_cell[i, j] is FieldCell:
                    if not (isBorderOfField(cell) or C.CountSteps != 0):
                        cell.setIcon(IconsForGame.ImgCross()) # заменить изображение в клетке на соответствующее
                        cell.CountSteps = 0 # обнуляем количество шагов на клетке
        Game.get_cell(self.i, self,j).setIcon(IconsForGame.ImgPlayer())