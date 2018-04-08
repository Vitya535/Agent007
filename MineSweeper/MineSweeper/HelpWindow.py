from PyQt5.QtWidgets import QWidget, QAction, QMenuBar

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


