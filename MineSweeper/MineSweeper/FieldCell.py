from PyQt5.QtWidgets import QPushButton, QMainWindow
from random import randint

class FieldCell(QPushButton):
    def __init__(self, CountSteps:str, **kwargs):
        return super().__init__(**kwargs)
        self.CountSteps = CountSteps
        # self.resize(30, 30)
        # self.setParent(MainWindow)
        # self.setText(CountSteps)
        # self.move(30*(i+1), 30*(j+1))