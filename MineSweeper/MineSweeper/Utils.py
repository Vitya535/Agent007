"""
Здесь расположены функции,
которые помогают в реализации
игры
"""


def is_border_of_field(cell, player, game) -> bool:
    """функция определяет, является ли клетка границей поля"""
    if (-1 <= player.i - cell.coord_i() <= 1 and -1 <= player.j - cell.coord_j() <= 1) and \
            (cell.coord_i() == 0 or cell.coord_i() == game.get_height() or cell.coord_j() == 0 or
             cell.coord_j() == game.get_width()):
        return True
    return False
