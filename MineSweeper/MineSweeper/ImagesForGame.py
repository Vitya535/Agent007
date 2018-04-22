from PyQt5.QtGui import QIcon

class IconsForGame(object):
    """description of class"""
    ImgMine, ImgCross, ImgPlayer, ImgSkull = QIcon('Images/Mine.png'), QIcon('Images/Cross.png'), QIcon('Images/Player.png'), QIcon('Images/Skull.jpg')

    @staticmethod
    def GetMine() -> QIcon:
        return IconsForGame.ImgMine

    @staticmethod
    def GetCross() -> QIcon:
        return IconsForGame.ImgCross

    @staticmethod
    def GetPlayer() -> QIcon:
        return IconsForGame.ImgPlayer

    @staticmethod
    def GetSkull() -> QIcon:
        return IconsForGame.ImgSkull

