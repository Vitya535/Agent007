import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMenuBar, QMainWindow, QMenu, QAction
from RulesWindow import RulesWindow
from Game import Game

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def SmallFieldClicked(self):
        Game.inst(10, 10, 5, self)  

    def MediumFieldClicked(self):
        Game.inst(15, 15, 7, self)

    def LargeFieldClicked(self):
        Game.inst(20, 20, 10, self)

    def initUI(self):
        self.resize(400, 400)
        self.move(300, 300)
        self.setWindowTitle('Агент 007')

        self.MenuForWindow = QMenuBar(self)
        self.MenuForWindow.resize(400, 25)

        self.RulesW = RulesWindow(self.MenuForWindow)
        self.HelpW = QMenu("Настройки", self.MenuForWindow)
        self.MenuForWindow.addMenu(self.HelpW)
        self.FieldMenu = QMenu("Параметры поля", self.HelpW)
        self.HelpW.addMenu(self.FieldMenu)

        self.SmallFieldAction = QAction("Маленькое (10x10), 5 мин", self.FieldMenu)
        self.MediumFieldAction = QAction("Среднее (15x15), 7 мин", self.FieldMenu)
        self.LargeFieldAction = QAction("Большое (20x20), 10 мин", self.FieldMenu)

        self.SmallFieldAction.triggered.connect(self.SmallFieldClicked)
        self.MediumFieldAction.triggered.connect(self.MediumFieldClicked)
        self.LargeFieldAction.triggered.connect(self.LargeFieldClicked)

        self.FieldMenu.addAction(self.SmallFieldAction)
        self.FieldMenu.addAction(self.MediumFieldAction)
        self.FieldMenu.addAction(self.LargeFieldAction)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyForm = MainForm()
    sys.exit(app.exec_())