import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMenuBar
from HelpWindow import HelpWindow
from RulesWindow import RulesWindow
from Game import Game

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    MainWindow = QWidget()
    MainWindow.resize(400, 400)
    MainWindow.move(300, 300)
    MainWindow.setWindowTitle('Агент 007')

    MenuForWindow = QMenuBar(MainWindow)
    MenuForWindow.resize(400, 25)

    RulesW, HelpW = RulesWindow(MenuForWindow), HelpWindow(MenuForWindow)

    if HelpW.close():
        MyGame = Game(HelpW.WidthValue.intValue(), HelpW.HeightValue.intValue(), HelpW.MinesCount.intValue(), MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())