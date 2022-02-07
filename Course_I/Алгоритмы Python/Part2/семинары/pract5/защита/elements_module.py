import numpy as np
from util_module import UtilClass


class FieldClass:
    """
    Класс одной клетки доски
    Поля:
    - Координата X
    - Координата Y
    - Занята или нет, если занята то кем?
    - Цвет клетки
    - Ссылка на объект фигуры, которая стоит на клетке

    Методы:
    - Занятие/резервация клетки фигурой
    - Освобождение клетки фигурой
    """

    def __init__(self, coord_x, coord_y, figure_obj=None):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.figure_obj = figure_obj
        self.color_generator()

    def color_generator(self):
        """Генератор цвета ячейки на основе ее координат"""
        x = UtilClass.char2xint(self.coord_x)
        y = self.coord_y

        if (x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
            color = "black"
        else:
            color = "white"

        self.color = color

    def isfree(self):
        """Проверяет, свободна ли текущая ячейка"""
        if self.figure_obj == None:
            return True
        return False

    def field_reserve(self, figure_obj):
        """Занятие клетки фигурой"""
        self.figure_obj = figure_obj

    def field_free(self):
        """Освобождение клетки фигурой"""
        self.figure_obj = None

    def __str__(self):
        """Вывод ячейки на экран"""
        board_color2print_dict = {"black": "⬛️", "white": "⬜️"}
        figure_color2print_dict = {"black": "🌚", "white": "🌝"}
        # Если ячейка свободная -> выводим просто ее цвет на экран
        if self.isfree():
            return board_color2print_dict[self.color]
        # Если ячейка занята -> выводим цвет шашки, которую она занимает
        return figure_color2print_dict[self.figure_obj.color]


class FigureClass:
    """
    Класс фигуры (шашки)
    Поля:
    - Координата X
    - Координата Y
    - Цвет (черный/белый) генерится автоматически
    """

    def __init__(self, color, coord_x, coord_y):
        self.color = color
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        return "Тип: *Шашка обыкновенная*\n*Координаты* x:{}, y:{}\n*Цвет* {}".format(
            self.coord_x, self.coord_y, self.color
        )


class BoardClass:
    """Класс игровой доски"""

    def __init__(self, generator_way, user_color):

        self.user_color = user_color
        figuregenerator_dict = {
            1: self.figuremanual_generator,
            2: self.figureauto_generator,
        }
        self.board = None
        self.board_generator()

        if generator_way in figuregenerator_dict:
            figuregenerator_dict[generator_way]()
        else:
            raise ValueError(
                "Нет запрашиваемого метода расстановки фигур {}!".format(generator_way)
            )

    def board_generator(self):
        """Создание чистого игрового поля без фигур"""
        board = np.array([])
        for x in np.arange(8):
            for y in np.arange(8):
                field_obj = FieldClass(UtilClass.xint2char(x), y)
                board = np.append(field_obj, board)
        self.board = np.array(board.reshape(8, 8))

    def detect_element(self, search_x, search_y):
        """
        Определяем, есть ли элемент с такими координатами на доске
        Это необходимо для того, чтоб не выехать за массив
        """
        if search_x not in range(0, 8) or search_y not in range(0, 8):
            return False

        search_x = UtilClass.xint2char(search_x)
        board = self.board
        for x in np.arange(board.shape[0]):
            for y in np.arange(board.shape[1]):
                if board[x][y].coord_x == search_x and board[x][y].coord_y == search_y:
                    return True
        return False

    def figureauto_generator(self):
        """Автоматическая расстановка 12 фигур по полю"""
        uc = self.user_color
        reverse_uc = "black" if uc == "white" else "white"

        board = self.board
        for x in np.arange(board.shape[0]):
            for y in np.arange(board.shape[1]):
                if x < 3 and (
                    (x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)
                ):
                    board[x][y].field_reserve(FigureClass(uc, x, y))
                elif x > 4 and (
                    (x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)
                ):
                    board[x][y].field_reserve(FigureClass(reverse_uc, x, y))
        self.board = board

    def boardfigure_setter(self, color, search_x, search_y):
        """
        Поиск координат фигуры и ее постановка
        Возврат True - фигура поставлена
        Возврат False - фигура с координатами не найдена
        """
        x = search_x
        y = UtilClass.char2xint(search_y)
        board = self.board

        if board[x][y].isfree() and board[x][y].color == "black":
            board[x][y].field_reserve(FigureClass(color, x, y))
            self.board = board
            return True

        if not board[x][y].isfree():
            print(
                "\033[91m[Ошибка]\033[0m Клетка с координатами {}{} уже занята".format(
                    search_y, search_x + 1
                )
            )

        if board[x][y].color == "white":
            print(
                "\033[91m[Ошибка]\033[0m Цвет клетки с координатами {}{} белый".format(
                    search_y, search_x + 1
                )
            )

        return False

    def figuremanual_generator(self):
        """Ручная расстановка 6 фигур по полю"""
        format_dict = {"white": "белого", "black": "чёрного"}
        for color in ("white", "black"):
            print(
                "\033[93m*Выставляем шашки {} цвета*\033[0m".format(format_dict[color])
            )
            for i in range(6):

                boolean_flag = True
                while boolean_flag:
                    print(self)
                    coord_input = input(
                        "Введите координаты расположения шашки №{} -> ".format(i + 1)
                    )
                    if UtilClass.checkxy_value(coord_input):
                        coord_x = int(coord_input[1]) - 1
                        coord_y = coord_input[0]
                        result = self.boardfigure_setter(color, coord_x, coord_y)
                        if result:
                            print(
                                "Успешная постановка шашки на координаты {}".format(
                                    coord_input
                                )
                            )
                            boolean_flag = False
                    else:
                        print(
                            "\033[91m[Ошибка]\033[0m Некорретный ввод данных, пример координат: h2"
                        )

    def __str__(self):
        """Вывод игровой доски не экран"""
        board = self.board
        for i in np.arange(board.shape[0] - 1, -1, -1):
            print("{}".format(i + 1), end="")
            for j in np.arange(board.shape[1]):
                print("{}".format(board[i][j]), end="")
            print("")
        print("  A B C D E F G H")
        return ""
