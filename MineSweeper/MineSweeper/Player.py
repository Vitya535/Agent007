from PyQt5.QtWidgets import QPushButton, QMainWindow
from ImagesForGame import IconsForGame
from FieldCell import FieldCell
from Utils import isClickedAroundPlayer, isBorderOfField
from Game import Game
from Mine import Mine

class Player(QPushButton):
    player = None

    @staticmethod
    def inst(text:str, i:int, j:int, MainWindow:QMainWindow):
        if Player.player is None:
            Player.player = Player(text, i, j, MainWindow)
        return Player.player

    def __init__(self, text:str, i:int, j:int, MainWindow:QMainWindow):
        return super().__init__(IconsForGame.ImgPlayer(), text, i, j, MainWindow)
        self.i = i
        self.j = j

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
                if Game.get_cell[i, j] is Mine:
                    print("1") # игрок погибает
                elif Game.get_cell[i, j] is FieldCell:
                    C = FieldCell(Game.get_cell[i, j])
                    if not (isBorderOfField(cell) or C.CountSteps != 0):
                        print("2")
                        # заменить изображение в клетке на соответствующее
                        cell.CountSteps = 0 # обнуляем количество шагов на клетке
                    else:
                        print("3") # игрок погибает