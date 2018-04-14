from PyQt5.QtWidgets import QWidget, QAction, QMenuBar, QLabel, QLCDNumber, QMenu, QPushButton

class HelpWindow(QWidget):
    """description of class"""

    @property
    def Action(self):
        return self.SettingsAction

    def __init__(self, Menu:QMenuBar, **kwargs):
        super().__init__(**kwargs)
        self.resize(400, 400)
        self.setWindowTitle('Настройки')
        self.SettingsAction = QAction("Настройки", Menu)
        self.SettingsAction.triggered.connect(self.show)
        Menu.addAction(self.SettingsAction)

        self.WidthLabel = QLabel("Ширина поля:", self)
        self.WidthLabel.move(5, 25)
        self.WidthValue = QLCDNumber(self)
        self.WidthValue.setNumDigits(6)
        self.WidthValue.move(5, 40)

        self.HeightLabel = QLabel("Высота поля:", self)
        self.HeightLabel.move(5, 65)
        self.HeightValue = QLCDNumber(self)
        self.HeightValue.setNumDigits(6)
        self.HeightValue.move(5, 80)

        self.MinesCountLabel = QLabel("Количество мин:", self)
        self.MinesCountLabel.move(5, 105)
        self.MinesCount = QLCDNumber(self)
        self.MinesCount.setNumDigits(6)
        self.MinesCount.move(5, 120)

        self.MenuForHelp = QMenuBar(self)
        self.MenuForHelp.resize(90, 25)
        self.MenuSizeField = QMenu("Размер поля", self.MenuForHelp)
        self.MenuForHelp.addMenu(self.MenuSizeField)

        self.ButtonOK = QPushButton("OK", self)
        self.ButtonOK.move(5, 150)

        self.SmallFieldAction = QAction("Маленькое", self.MenuSizeField)
        self.MediumFieldAction = QAction("Среднее", self.MenuSizeField)
        self.LargeFieldAction = QAction("Большое", self.MenuSizeField)

        self.SmallFieldAction.triggered.connect(self.SmallFieldClicked)
        self.MediumFieldAction.triggered.connect(self.MediumFieldClicked)
        self.LargeFieldAction.triggered.connect(self.LargeFieldClicked)

        self.MenuSizeField.addAction(self.SmallFieldAction)
        self.MenuSizeField.addAction(self.MediumFieldAction)
        self.MenuSizeField.addAction(self.LargeFieldAction)
        self.ButtonOK.clicked.connect(self.close)

    def SmallFieldClicked(self):
        self.WidthValue.display(10)
        self.HeightValue.display(10)
        self.MinesCount.display(10)

    def MediumFieldClicked(self):
        self.WidthValue.display(30)
        self.HeightValue.display(30)
        self.MinesCount.display(30)

    def LargeFieldClicked(self):
        self.WidthValue.display(50)
        self.HeightValue.display(50)
        self.MinesCount.display(50)




