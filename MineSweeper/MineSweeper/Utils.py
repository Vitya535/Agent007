from Player import *
from FieldCell import FieldCell
from Game import *

@staticmethod
def isClickedAroundPlayer(cell:FieldCell)->tuple:
        if (Player.player.i - cell.i < -1 or Player.player.i - cell.i > 1) and (Player.player.j - cell.j < -1 or Player.player.j - cell.j > 1):
            return False, None, None
        else:
            return True, Player.player.i - cell.i, Player.player.j - cell.j

@staticmethod
def isBorderOfField(cell:FieldCell)->bool:
    if cell.i == 0 or cell.i == Game.get_height() or cell.j == 0 or cell.j == Game.get_width():
        return True
    else:
        return False