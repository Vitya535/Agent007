"""
Данный класс является
основным для игры Агент_007
в нем содержится все что
связано с формой
"""
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from MineSweeper.game import MyGame


class MainForm(QMainWindow):
    """
    Этот класс описывает основную форму
    данного приложения
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def reset_my_game(self):
        """
        Данный метод при его вызове
        заново пересоздает поле из кнопок
        с тем же размером и количеством мин,
        которое было изначально
        """
        self.RulesWindow.hide()
        MyGame._MyGame__instance = None  # доступ может поправить?
        MyGame.inst(MyGame.buf_instance.get_width(), MyGame.buf_instance.get_height(),
                    MyGame.buf_instance.get_mines_count(), self)

    def small_field_clicked(self):
        """
        Данный метод создает поле из кнопок
        размером 10х10, с 5 минами и игроком
        """
        self.RulesWindow.hide()
        MyGame.inst(10, 10, 5, self)
        self.BoxesValue.setText("94")
        self.GoalValue.setText("23")
        self.BoxesPercent.setText("94%")
        self.GoalPercent.setText("23%")

    def medium_field_clicked(self):
        """
        Данный метод создает поле из кнопок
        размером 15х15, с 7 минами и игроком
        """
        self.RulesWindow.hide()
        MyGame.inst(15, 15, 7, self)
        self.BoxesValue.setText("217")
        self.GoalValue.setText("54")
        self.BoxesPercent.setText(str(int(217/225*100)) + "%")
        self.GoalPercent.setText(str(int(54/225*100)) + "%")

    def large_field_clicked(self):
        """
        Данный метод создает поле из кнопок
        размером 20х20, с 10 минами и игроком
        """
        self.RulesWindow.hide()
        MyGame.inst(20, 20, 10, self)
        self.BoxesValue.setText("389")
        self.GoalValue.setText("97")
        self.BoxesPercent.setText(str(int(389/400*100)) + "%")
        self.GoalPercent.setText(str(int(97/400*100)) + "%")

    def init_ui(self):
        """
        Данный метод загружает форму и
        все связанные с ее компонентами события
        и выводит ее на экран
        """
        loadUi('MyMainForm.ui', self)
        self.RulesWindow.hide()
        self.SmallFieldAction.triggered.connect(self.small_field_clicked)
        self.MediumFieldAction.triggered.connect(self.medium_field_clicked)
        self.LargeFieldAction.triggered.connect(self.large_field_clicked)

        self.FieldMenu.addAction(self.SmallFieldAction)
        self.FieldMenu.addAction(self.MediumFieldAction)
        self.FieldMenu.addAction(self.LargeFieldAction)

        self.ResetButton.clicked.connect(self.reset_my_game)
        self.field.hide()

        self.showMaximized()


if __name__ == "__main__":
    MY_APP = QApplication(sys.argv)
    MY_FORM = MainForm()
    sys.exit(MY_APP.exec_())
