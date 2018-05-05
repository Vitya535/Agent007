"""
Данный модуль отвечает за логику игры
также он содержит в себе различные типы
ячеек (кнопок)
"""
from random import randint
from PyQt5.QtWidgets import QPushButton
from MineSweeper.utils import is_border_of_field


class MyGame:
    """
    Данный класс инициализирует игру
    содержит в себе все что связано с ней
    """
    __instance = None
    buf_instance = None

    @staticmethod
    def get_buf():
        """возврат буфера игры"""
        return MyGame.buf_instance

    @staticmethod
    def get_instance():
        """возврат ссылки на основной экземпляр игры"""
        return MyGame.__instance

    @staticmethod
    def inst(width: int, height: int, mines_count: int, main_window):
        """реализация одиночки для инициализации игры"""
        if MyGame.__instance is None:
            MyGame.__instance = MyGame(width, height, mines_count, main_window)
            MyGame.buf_instance = MyGame(width, height, mines_count, main_window)
        return MyGame.__instance

    def __init__(self, width: int, height: int, mines_count: int, main_window):
        self.main_window = main_window
        self.mines_count = mines_count
        self.width = width
        self.height = height
        self.main_window.field.setRowCount(height)
        self.main_window.field.setColumnCount(width)
        self.main_window.field.setFixedSize(38 * width, 38 * height)
        self.count_box = width * height - mines_count - 1
        self.score = 0
        self.main_window.field.setCellWidget(0, 0, MyPlayer.inst(main_window))
        counter_of_mines, k = 0, 1
        for i in range(height):  # строки  # кажется здесь как-то не так ячейки в поле заполняются
            for j in range(k, width):  # столбцы
                rand_for_mine = randint(1, 7)
                if rand_for_mine == 1 and counter_of_mines < mines_count:
                    self.main_window.field.setCellWidget(i, j, MyMine(i, j, main_window))
                    counter_of_mines += 1
                else:
                    rand_for_cells = randint(1, 6)
                    self.main_window.field.setCellWidget(i, j, MyCell(rand_for_cells, i, j, main_window))
            k = 0
        self.main_window.field.show()

    @property
    def get_mines_count(self) -> int:
        """возвращает количество мин на поле"""
        return self.mines_count

    @property
    def get_width(self) -> int:
        """возвращает ширину поля"""
        return self.width

    @property
    def get_height(self) -> int:
        """возвращает высоту поля"""
        return self.height

    @staticmethod
    def count_score_and_boxes(boxes: list):
        """подсчет очков и количества не обойденных клеток игроком"""
        MyGame.__instance.count_box -= len(boxes)
        MyGame.__instance.score += sum(boxes) * 10
        MyGame.__instance.main_window.BoxesValue.setText(str(MyGame.__instance.count_box))
        MyGame.__instance.main_window.ScoreValue.setText(str(MyGame.__instance.score))
        MyGame.__instance.main_window.BoxesPercent.setText(str(int(
            MyGame.__instance.count_box / (MyGame.__instance.width * MyGame.__instance.height) * 100)) +
                                                           "%")


class MyPlayer(QPushButton):
    """Класс клетки-игрока на поле"""

    player = None

    @staticmethod
    def inst(main_window):
        """реализация одиночки в игре для инициализации"""
        if MyPlayer.player is None:
            MyPlayer.player = MyPlayer(main_window)
        return MyPlayer.player

    def __init__(self, main_window):
        super().__init__(main_window)
        self.init_player()
        self.i, self.j = 0, 0

    def init_player(self):
        """инициализация клетки-игрока на поле"""
        self.setText("Player")
        self.setFixedSize(38, 38)

    @property
    def coord_i(self) -> int:
        """возвращает кооординату игрока по строке"""
        return self.i

    @property
    def coord_j(self) -> int:
        """возвращает кооординату игрока по столбцу"""
        return self.j

    def move_to(self, cell):
        """Данный метод отвечает за передвижение игрока по клеткам"""
        ins = MyGame.get_instance()
        _boxes = []
        diff_row, diff_column = self.i - cell.i, self.j - cell.j
        limit_row, limit_column = self.i - diff_row * cell.count_steps, self.j - diff_column * cell.count_steps
        while self.i != limit_row or self.j != limit_column:
            _cell = ins.main_window.field.cellWidget(self.i, self.j)
            if _cell.__class__ == MyMine or is_border_of_field(diff_row, diff_column, _cell, ins) or \
                    _cell.text() == "Cross":
                _cell.setText("Skull")
                MyGame.count_score_and_boxes(_boxes)
                return
            else:
                if _cell.__class__ == MyCell and _cell.text() != "Player":
                    _boxes.append(_cell.count_steps)
                if self.i != _cell.i and self.j != _cell.j and _cell.__class__ == MyCell:
                    _cell.clicked.disconnect(_cell.is_clicked_around_player)
                _cell.setText("Cross")
            self.j -= diff_column
            self.i -= diff_row
        _cell = ins.main_window.field.cellWidget(self.i, self.j)
        _cell.setText("Player")
        if _cell.__class__ == MyCell:
            _cell.clicked.disconnect(_cell.is_clicked_around_player)
            _boxes.append(_cell.count_steps)
        MyGame.count_score_and_boxes(_boxes)


class MyCell(QPushButton):
    """класс ячейки с количеством шагов"""

    def __init__(self, count_steps: int, i: int, j: int, main_window):
        super().__init__(main_window)
        self.init_field_cell(count_steps)
        self.count_steps, self.i, self.j = count_steps, i, j

    def init_field_cell(self, count_steps: int):
        """инициализация ячейки на поле"""
        self.setText(str(count_steps))
        self.setFixedSize(38, 38)
        self.clicked.connect(self.is_clicked_around_player)

    @property
    def get_count_of_steps(self) -> int:
        """возвращает количество шагов у этой кнопки"""
        return self.count_steps

    @property
    def coord_i(self) -> int:
        """возвращает координату ячейки по строке"""
        return self.i

    @property
    def coord_j(self) -> int:
        """возвращает координату ячейки по столбцу"""
        return self.j

    def is_clicked_around_player(self):
        """Проверка на нажатие кнопки рядом с игроком"""
        if self.text() != "Cross" and \
                MyGame.get_instance().main_window.field.cellWidget(MyPlayer.player.i,
                                                                   MyPlayer.player.j).text() != "Skull":
            if -1 <= MyPlayer.player.i - self.i <= 1 and -1 <= MyPlayer.player.j - self.j <= 1:
                MyPlayer.player.move_to(self)


class MyMine(QPushButton):
    """класс ячейки-мины на поле"""

    def __init__(self, i: int, j: int, main_window):
        super().__init__(main_window)
        self.init_mine()
        self.i, self.j = i, j

    def init_mine(self):
        """инициализация мины на поле"""
        self.setText("Mine")
        self.setFixedSize(38, 38)

    @property
    def coord_i(self) -> int:
        """возвращает координату мины по строке"""
        return self.i

    @property
    def coord_j(self) -> int:
        """возвращает координату мины по столбцу"""
        return self.j
