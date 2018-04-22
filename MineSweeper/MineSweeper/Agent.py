import sys
from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QMenu, QAction, QLabel
from PyQt5.QtGui import QFont
from RulesWindow import RulesWindow
from Game import MyGame

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def SmallFieldClicked(self):
        MyGame.inst(10, 10, 5, self)
        self.BoxesValue.setText("94")
        self.GoalValue.setText("23")     

    def MediumFieldClicked(self):
        MyGame.inst(15, 15, 7, self)
        self.BoxesValue.setText("217")
        self.GoalValue.setText("54") 

    def LargeFieldClicked(self):
        MyGame.inst(20, 20, 10, self)
        self.BoxesValue.setText("389")
        self.GoalValue.setText("97") 

    def initUI(self):
        self.setMinimumSize(400, 400)
        self.move(300, 300)
        self.setWindowTitle('Агент 007')

        self.MenuForWindow = QMenuBar(self)
        self.MenuForWindow.resize(16777215, 25)

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

        self.SpyLabel = QLabel("Spy", self)
        self.SpyLabel.move(1100, 50)
        self.SpyLabel.setFixedSize(300, 100)
        fontspy = QFont()
        fontspy.setPointSize(60)
        self.SpyLabel.setFont(fontspy)

        self.BoxesLabel = QLabel("Boxes:", self)
        self.BoxesLabel.move(900, 150)
        self.BoxesLabel.setFixedSize(300, 100)
        fontbox = QFont()
        fontbox.setPointSize(60)
        self.BoxesLabel.setFont(fontbox)

        self.GoalLabel = QLabel("Goal:", self)
        self.GoalLabel.move(900, 250)
        self.GoalLabel.setFixedSize(300, 100)
        fontgoal = QFont()
        fontgoal.setPointSize(60)
        self.GoalLabel.setFont(fontgoal)

        self.ScoreLabel = QLabel("Score:", self)
        self.ScoreLabel.move(900, 350)
        self.ScoreLabel.setFixedSize(300, 100)
        fontscore = QFont()
        fontscore.setPointSize(60)
        self.ScoreLabel.setFont(fontscore)

        self.BoxesValue = QLabel("0", self)
        self.BoxesValue.move(1150, 150)
        self.BoxesValue.setFixedSize(300, 100)
        fontboxvalue = QFont()
        fontboxvalue.setPointSize(60)
        self.BoxesValue.setFont(fontboxvalue)

        self.GoalValue = QLabel("0", self)
        self.GoalValue.move(1100, 250)
        self.GoalValue.setFixedSize(300, 100)
        fontgoalvalue = QFont()
        fontgoalvalue.setPointSize(60)
        self.GoalValue.setFont(fontgoalvalue)

        self.ScoreValue = QLabel("0", self)
        self.ScoreValue.move(1150, 350)
        self.ScoreValue.setFixedSize(300, 100)
        fontscorevalue = QFont()
        fontscorevalue.setPointSize(60)
        self.ScoreValue.setFont(fontscorevalue)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyForm = MainForm()
    sys.exit(app.exec_())