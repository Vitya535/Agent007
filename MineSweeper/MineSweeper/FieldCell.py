from PyQt5.QtWidgets import QPushButton, QMainWindow

class FieldCell(QPushButton):
    def __init__(self, CountSteps:int, i:int, j:int, MainWindow:QMainWindow):
        return super().__init__(str(CountSteps), MainWindow)
        self.CountSteps = CountSteps
        self.i = i
        self.j = j

    @property
    def getCountOfSteps(self)->int:
        return self.CountSteps

    @property
    def get_X(self)->int:
        return self.i

    @property
    def get_Y(self)->int:
        return self.j