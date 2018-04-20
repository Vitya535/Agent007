from PyQt5.QtGui import QIcon 

class IconsForGame():
    Mine, Player, Cross, Skull = QIcon('Images/Mine.png'), QIcon('Images/Player.png'), QIcon('Images/Cross.png'), QIcon('Images/Skull.jpg')

    @property
    def ImgMine()->QIcon:
        return IconsForGame.Mine

    @property
    def ImgPlayer()->QIcon:
        return IconsForGame.Player

    @property
    def ImgCross()->QIcon:
        return IconsForGame.Cross

    @property
    def ImgSkull()->QIcon:
        return IconsForGame.Skull

