from PyQt5.QtWidgets import QTextBrowser, QAction, QMenuBar
from PyQt5.QtCore import QUrl

class RulesWindow(QTextBrowser):
    """description of class"""
    
    @property
    def Action(self):
        return self.RulesAction

    def __init__(self, Menu:QMenuBar, **kwargs):
        super().__init__(**kwargs)
        self.resize(400, 400)
        self.setWindowTitle('Правила игры')
        self.setSource(QUrl.fromLocalFile("C:/Users/Виктор/Desktop/Университет/4семестр/Питон/1Аттестация/MineSweeper/MineSweeper/MineSweeper/Rules.html"))
        self.RulesAction = QAction("Правила", Menu)
        self.RulesAction.triggered.connect(self.show)
        Menu.addAction(self.RulesAction)


