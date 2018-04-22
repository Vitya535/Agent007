from Game import *

def isClickedAroundPlayer(player, cell) -> bool:
    if ((-1 <= player.get_X - cell.X <= 1) and (player.get_Y - cell.Y == -1 or player.get_Y - cell.Y == 1)) or ((player.get_X - cell.X == 1 or player.get_X - cell.X == -1) and player.get_Y - cell.Y == 0):
        return True
    return False

def isBorderOfField(cell) -> bool:
    if cell.X == 0 or cell.X == MyGame.get_height() or cell.Y == 0 or cell.Y == MyGame.get_width():
        return True
    return False


